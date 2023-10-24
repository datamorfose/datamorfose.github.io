

import pytest
from utils_dbstreams import StreamsUtils
import json

stream_utils = StreamsUtils()

record = {'eventID': 'ed8985c7099e2036908bfac81ae7d19e', 'eventName': 'INSERT', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-2', 'dynamodb': {'ApproximateCreationDateTime': 1698112613.0, 'Keys': {'account_id': {'S': 'conta#00019'}, 'sk': {'S': 'JANELA#ALL'}}, 'NewImage': {'account_id': {'S': 'conta#00019'}, 'sk': {'S': 'JANELA#ALL'}, 'valor': {'L': [{'M': {'qtd': {'N': '10'}, 'janela': {'S': '1h'}}}, {'M': {'qtd': {'N': '30'}, 'janela': {'S': '3h'}}}, {'S': 'teste'}]}, 'dt_inclusao': {'S': '2023-01-09 10:56:56'}}, 'SequenceNumber': '24150200000000005715226765', 'SizeBytes': 148, 'StreamViewType': 'NEW_IMAGE'}, 'eventSourceARN': 'arn:aws:dynamodb:us-east-2:750204280754:table/teste_dbstreams/stream/2023-10-19T00:03:47.027'}

image = {'account_id': {'S': 'conta#00019'}, 'sk': {'S': 'JANELA#ALL'}, 'valor': {'L': [{'M': {'qtd': {'N': '10'}, 'janela': {'S': '1h'}}}, {'M': {'qtd': {'N': '30'}, 'janela': {'S': '3h'}}}, {'S': 'teste'}]}, 'dt_inclusao': {'S': '2023-01-09 10:56:56'}}

valor = [{'M': {'qtd': {'N': '10'}, 'janela': {'S': '1h'}}}, {'M': {'qtd': {'N': '30'}, 'janela': {'S': '3h'}}}, {'S': 'teste'}]

def test_generate_data():
    
    result = stream_utils.generate_data(record)
    expected_result = '{"id_conta": "00019", "janelas": [{"qtd": "10", "janela": "1h"}, {"qtd": "30", "janela": "3h"}], "dt_inclusao": "2023-01-09 10:56:56"}'
    assert result == expected_result

def test_get_image():
    id_conta, valor, dt_inclusao = stream_utils.get_image(image)
    assert id_conta == 'conta#00019'
    assert valor == [{'M': {'qtd': {'N': '10'}, 'janela': {'S': '1h'}}}, {'M': {'qtd': {'N': '30'}, 'janela': {'S': '3h'}}}, {'S': 'teste'}]
    assert dt_inclusao == '2023-01-09 10:56:56'

def test_process_values():
    values_data = stream_utils.process_values(valor)
    expected_result = [
        {'qtd': '10', 'janela': '1h'},
        {'qtd': '30', 'janela': '3h'}
    ]
    assert values_data == expected_result


def test_get_image_unhappy_path_missing_fields():
    image = {
        'account_id': {'S': 'conta#00019'},
        'valor': {'L': []},  # Simula valor ausente
        'dt_inclusao': {'S': '2023-01-09 10:56:56'}
    }
    with pytest.raises(ValueError):
        stream_utils.get_image(image)

def test_process_values_unhappy_path_invalid_type():
    valor = {'M': {'qtd': {'N': '10'}, 'janela': {'S': '1h'}}, 'S': 'teste'}  # Simula formato inválido
    with pytest.raises(TypeError):
        stream_utils.process_values(valor)

def test_process_values_unhappy_path_invalid_value():
    valor = {'L': [{'S': 'teste'}, {'N': '12'}]}
    result = stream_utils.process_values(valor)
    assert result == []  # A função deve retornar uma lista vazia

@pytest.fixture
def record():
    record = {'eventID': 'e3257fe689b8e099cc310e05c132517a', 'eventName': 'INSERT', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-2', 'dynamodb': {'ApproximateCreationDateTime': 1698148210.0, 'Keys': {'account_id': {'S': 'conta#00022222'}, 'sk': {'S': 'JANELA#ALL'}}, 'NewImage': {'account_id': {'S': 'conta#00022222'}, 'sk': {'S': 'JANELA#ALL'}, 'valor': {'L': [{'S': 'teste'}, {'N': '12'}]}, 'dt_inclusao': {'S': '2023-01-09 10:56:56'}}, 'SequenceNumber': '25787000000000013143919731', 'SizeBytes': 119, 'StreamViewType': 'NEW_IMAGE'}, 'eventSourceARN': 'arn:aws:dynamodb:us-east-2:750204280754:table/teste_dbstreams/stream/2023-10-19T00:03:47.027'}
    return record

def test_generate_data_empty_janelas(record):
    with pytest.raises(ValueError):
        StreamsUtils().generate_data(record)