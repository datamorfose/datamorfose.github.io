import json
from db_streams_service import DbStreamsService
import pytest

@pytest.fixture
def record() -> dict:
    return {'eventID': 'c9e18260abe4f8d131e3554608217feb', 'eventName': 'INSERT', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-2', 'dynamodb': {'ApproximateCreationDateTime': 1698806932.0, 'Keys': {'account_id': {'S': 'conta#00131SN068'}, 'sk': {'S': 'JANELA#ALL'}}, 'NewImage': {'account_id': {'S': 'conta#00131SN068'}, 'sk': {'S': 'JANELA#ALL'}, 'valor': {'L': [{'M': {'qtd_vdce': {'N': '12'}, 'ratio_vdcne_vdc': {'N': '3.01'}, 'ratio_vdc_eos': {'N': '1.85'}, 'qtd_vdc': {'N': '10'}, 'qtd_vdcne': {'N': '121'}, 'qtd_eos': {'N': '12'}, 'janela': {'S': '1h'}}}, {'M': {'qtd_vdce': {'N': '22'}, 'ratio_vdcne_vdc': {'N': '3.901'}, 'ratio_vdc_eos': {'N': '2.85'}, 'qtd_vdc': {'N': '30'}, 'qtd_vdcne': {'N': '131'}, 'qtd_eos': {'N': '32'}, 'janela': {'S': '3h'}}}, {'NULL': True}, {'S': 'null'}]}, 'dt_inclusao': {'S': '2023-01-09 10:56:56'}}, 'SequenceNumber': '62126400000000028252209088', 'SizeBytes': 308, 'StreamViewType': 'NEW_IMAGE'}, 'eventSourceARN': 'arn:aws:dynamodb:us-east-2:750204280754:table/teste_dbstreams/stream/2023-10-19T00:03:47.027'}

@pytest.fixture
def expected_data() -> dict:
    return {
    "data": {
        "account_id": "00131SN068",
        "dt_inclusao": "2023-01-09 10:56:56",
        "janelas": [
            {
                "qtd_vdce": 12,
                "ratio_vdcne_vdc": 3.01,
                "ratio_vdc_eos": 1.85,
                "qtd_vdc": 10,
                "qtd_vdcne": 121,
                "qtd_eos": 12,
                "janela": "1h"
            },
            {
                "qtd_vdce": 22,
                "ratio_vdcne_vdc": 3.901,
                "ratio_vdc_eos": 2.85,
                "qtd_vdc": 30,
                "qtd_vdcne": 131,
                "qtd_eos": 32,
                "janela": "3h"
            }
        ]
    }
}

@pytest.fixture
def record_image():
    return {'account_id': {'S': 'conta#00131SN068'}, 'sk': {'S': 'JANELA#ALL'}, 'valor': {'L': [{'M': {'qtd_vdce': {'N': '12'}, 'ratio_vdcne_vdc': {'N': '3.01'}, 'ratio_vdc_eos': {'N': '1.85'}, 'qtd_vdc': {'N': '10'}, 'qtd_vdcne': {'N': '121'}, 'qtd_eos': {'N': '12'}, 'janela': {'S': '1h'}}}, {'M': {'qtd_vdce': {'N': '22'}, 'ratio_vdcne_vdc': {'N': '3.901'}, 'ratio_vdc_eos': {'N': '2.85'}, 'qtd_vdc': {'N': '30'}, 'qtd_vdcne': {'N': '131'}, 'qtd_eos': {'N': '32'}, 'janela': {'S': '3h'}}}, {'NULL': True}, {'S': 'null'}]}, 'dt_inclusao': {'S': '2023-01-09 10:56:56'}}

@pytest.fixture
def stream_service():
    stream_service = DbStreamsService()
    return stream_service

def test_generate_data_happy_path(record, expected_data, stream_service):
    
    
    data = stream_service.generate_data(record)
    assert isinstance(data, dict) 
    assert data == expected_data

def test_record_handler_positive(record_image, expected_data, stream_service):
    result = stream_service.record_handler(record_image)
    assert isinstance(result, str)
    result_dict = json.loads(result)
    assert result_dict == expected_data

#def test_dynamo_obj_to_python_obj():