#lambda_function.py 
import json
from db_streams_service import DbStreamsService
import logging
import os
#import boto3

#sqs = boto3.client('sqs')

stream_service = DbStreamsService()


def lambda_handler(event, context):

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Define o nível de log para DEBUG

    logger.debug(event)
    results = []
           
    try:
        #results = [stream_service.generate_data(record) for record in event['Records'] if record['eventName'] == 'INSERT']
        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                try:
                    result = stream_service.generate_data(record)
                    results.append(result)
                except Exception as e:
                    raise e

        logger.debug(results)
        logger.debug("------data's--------")
        print(*results, sep="\n")        
        #return results
    
        
    except Exception as e:
        return {
            "statusCode": 500,
            "Error": type(e).__name__,
            "errorMessage": str(e)
        }
        
    else:
        return {
            "statusCode": 200,
            "results": results
        }
        
    
#def send_failed_record_to_sqs(record):
#    queue_url = 'https://sqs.us-east-2.amazonaws.com/750204280754/fila-dbstreams'  # Substitua pela URL da sua fila SQS
#    response = sqs.send_message(
#        QueueUrl=queue_url,
#        MessageBody=json.dumps(record)  # Envie o registro falhado para a fila
#    )    
#
#def handle_failed_record(record):
#    try:
#        # Seu tratamento de registro falhado aqui
#        send_failed_record_to_sqs(record)
#    except Exception as e:
#        # Lidar com exceções de envio para SQS, se necessário
#        pass