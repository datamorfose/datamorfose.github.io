#db_streams_service.py
import json
import logging
from boto3.dynamodb.types import TypeDeserializer
from decimal import Decimal
from jsonschema import validate
import traceback

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Define o nível de log para DEBUG

schema = {
    "type": "object",
     "propertyNames": {
        "pattern": "^data.*$"
    },
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "account_id": {
                    "type": "string"
                },
                "janelas": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "qtd_vdc": {
                                "type": "integer"
                            },
                            "qtd_vdce": {
                                "type": "integer"
                            },
                            "qtd_vdcne": {
                                "type": "integer"
                            },
                            "qtd_eos": {
                                "type": "integer"
                            },
                            "ratio_vdc_eos": {
                                "type": "number"
                            },
                            "ratio_vdcne_vdc": {
                                "type": "number"
                            },
                            "janela": {
                                "type": "string"
                            }
                        },
                        "required": ["janela", "qtd_vdce"]
                    }
                },
                "dt_inclusao": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": ["account_id", "janelas", "dt_inclusao"]
        }
    }
}



class DbStreamsService:

        
    def generate_data(self, record) -> dict:
        try:
            
            logger.debug(f"Record: {record}")
            record_image = record['dynamodb']['NewImage']
            logger.debug(f"Record Image: {record_image}")

            data = self.record_handler(record_image)

            logger.debug(f"Data type: {type(data)}")
            logger.debug(f"Data: {data}")

            data = json.loads(data)
            
            return data
                
                
        except Exception as e:
            logging.error(f"Erro ao processar record: {str(e)}")
            logger.error(traceback.print_exc())
            raise e
    

    def data_schema_validation(self, data, schema):
        try:
            validate(data, schema)
            logger.debug("Schema válido")
        except jsonschema.exceptions.ValidationError as e:
            logging.error(repr(e))
            #logger.error(traceback.print_exc())
            raise RuntimeError("Schema não é válido")       


    def record_handler(self, record: dict) -> dict:
        record_obj = self.dynamo_obj_to_python_obj(record)
        #remove sk
        if 'sk' in record_obj:
            del record_obj['sk']
        #trata accound_id
        record_obj['account_id'] = record_obj['account_id'].split('#')[1]



        #trata valor

     
        if 'valor' in record_obj:
            record_obj['janelas'] = record_obj['valor']
            del record_obj['valor']
            logger.debug(f"Record obj: {record_obj}")
        else:        
            raise ValueError("Chave 'valor' não encontrada no registro")
        



        #trata null e "null" em janelas
        record_obj['janelas'] = [janela for janela in record_obj['janelas'] if janela is not None and janela != "null"]
        logger.debug(f"Janela tratada {record_obj}")

        #retorna record tratado
        #record_obj_float = json.dumps(record_obj, default=self.convert_decimal)
        #record_json = json.loads(record_obj_float)

        #data_schema_validation(record_obj_float, schema)

        #gera data
        data = {
            "data": record_obj
        }

        data = json.dumps(data, default=self.convert_decimal_to_int_or_float)
        logger.debug(f" DATAzzzzz: {data}")
        logger.debug(f"TYPE DATAzzz: {type(data)}")

        #data = json.dumps(data)

        return data


        
    def dynamo_obj_to_python_obj(self, dynamo_obj: dict) -> dict:
        deserializer = TypeDeserializer()
        return {
            k: deserializer.deserialize(v) 
            for k, v in dynamo_obj.items()
        }      
    
    def convert_decimal_to_int_or_float(self, obj):
        if isinstance(obj, Decimal):
            if obj % 1 == 0:
                return int(obj)
            return float(obj)
        raise TypeError


    #def convert_decimal_to_float(self, obj):
    #    if isinstance(obj, Decimal):
    #        return float(obj)
    #    raise TypeError
    #
    #def convert_decimal_to_int(self, obj):
    #    if isinstance(obj, Decimal):
    #        return int(obj)
    #    raise TypeError
    
    