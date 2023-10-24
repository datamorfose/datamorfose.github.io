#utils_dbstreams.py
import json
import logging

class StreamsUtils:

    def __init__(self):
        self.record =  None


    #Função para processar o registro do insert
    def generate_data(self, record) -> dict:
        try:
            if record is not None:
                id_conta, valor, dt_inclusao = self.get_image(record['dynamodb']['NewImage'])
                id_conta = id_conta.split('#')[1]
                janelas = self.process_values(valor)

                if not janelas:
                    raise ValueError("Nenhuma janela válida encontrada. Pulando este registro.")
                
                output_dict = {
                    "id_conta": id_conta,
                    "janelas": janelas,
                    "dt_inclusao": dt_inclusao
                }
                print(f"o tipo do output_dict é {type(output_dict)}")    
                
                data = json.dumps(output_dict, ensure_ascii=False)
                print(f"o tipo do  data é {type(data)}") 
                return data
                
        except Exception as e:
            logging.error(f"Erro ao processar evento de inserção: {str(e)}")
            raise


    #Função para ler o Record do DynamoDB Streams e recuperar atributos        
    def get_image(self, image):
        
        id_conta = image['account_id']['S']
        valor = image['valor']['L']
        dt_inclusao = image['dt_inclusao']['S']

        if not (id_conta and valor and dt_inclusao):
            error_msg = "Um ou mais valores estão vazios ou nulos"
            raise ValueError(error_msg)

        return id_conta, valor, dt_inclusao
      



    #Função para processar os valores da lista "valor" e recuperar as janelas gravadas no Record    
    def process_values(self, valor) -> list:
        values_data = []
        for item in valor:
            if 'M' in item:
                value_map = {}
                for map_item in item['M']:
                    value_map[map_item] = list(item['M'][map_item].values())[0]
                if value_map:
                    values_data.append(value_map)
        print(f"o tipo do values_data é {type(values_data)}")                
        return values_data    