#lambda_function.py

import json
from utils_dbstreams import StreamsUtils



def lambda_handler(event, context):
             
    try:
        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                data = StreamsUtils().generate_data(record)
                print(data)
                print(f"o tipo do  data2 é {type(data)}") 
                return data
    except Exception as e:
        print(e)
        
        return 200
        

