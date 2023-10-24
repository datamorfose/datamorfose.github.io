from lambda_function import lambda_handler
import pytest


@pytest.fixture
def event():
    event = {'Records': [{'eventID': '812ac47982c6cb84536e44740b704c1f', 'eventName': 'INSERT', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-2', 'dynamodb': {'ApproximateCreationDateTime': 1698147427.0, 'Keys': {'account_id': {'S': 'conta#00020'}, 'sk': {'S': 'JANELA#ALL'}}, 'NewImage': {'account_id': {'S': 'conta#00020'}, 'sk': {'S': 'JANELA#ALL'}, 'valor': {'L': [{'M': {'qtd': {'N': '10'}, 'janela': {'S': '1h'}}}, {'M': {'qtd': {'N': '30'}, 'janela': {'S': '3h'}}}, {'S': 'teste'}]}, 'dt_inclusao': {'S': '2023-01-09 10:56:56'}}, 'SequenceNumber': '25786900000000013143678962', 'SizeBytes': 148, 'StreamViewType': 'NEW_IMAGE'}, 'eventSourceARN': 'arn:aws:dynamodb:us-east-2:750204280754:table/teste_dbstreams/stream/2023-10-19T00:03:47.027'}]}

    return  event


def test_lambda_handler_success(event):
   
    context = {}
    # Chame a função lambda_handler com o evento simulado
    result = lambda_handler(event, context)
    # Verifique se o resultado é o que você espera
    expected_result = '{"id_conta": "00020", "janelas": [{"qtd": "10", "janela": "1h"}, {"qtd": "30", "janela": "3h"}], "dt_inclusao": "2023-01-09 10:56:56"}'
    assert result == expected_result

@pytest.fixture
def event_with_empty_janelas():
    event = {'Records': [{'eventID': 'e3257fe689b8e099cc310e05c132517a', 'eventName': 'INSERT', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-2', 'dynamodb': {'ApproximateCreationDateTime': 1698148210.0, 'Keys': {'account_id': {'S': 'conta#00022222'}, 'sk': {'S': 'JANELA#ALL'}}, 'NewImage': {'account_id': {'S': 'conta#00022222'}, 'sk': {'S': 'JANELA#ALL'}, 'valor': {'L': [{'S': 'teste'}, {'N': '12'}]}, 'dt_inclusao': {'S': '2023-01-09 10:56:56'}}, 'SequenceNumber': '25787000000000013143919731', 'SizeBytes': 119, 'StreamViewType': 'NEW_IMAGE'}, 'eventSourceARN': 'arn:aws:dynamodb:us-east-2:750204280754:table/teste_dbstreams/stream/2023-10-19T00:03:47.027'}]}
    return event

def test_lambda_handler_empty_janelas(event_with_empty_janelas):
    context = {}
    result = lambda_handler(event_with_empty_janelas, context)
    assert result == 200