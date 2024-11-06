import pytest
from unittest import mock
from codigo4 import *

def test_calcular_valor_total():
    mock_response = [
        {"preco": 10.0, "quantidade": 2},
        {"preco": 5.0, "quantidade": 1},
        {"preco": 20.0, "quantidade": 3}
    ]
    
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_response
        resultado = calcular(1)
        
    #(10 * 2) + (5 * 1) + (20 * 3) = 20 + 5 + 60 = 85
    assert resultado == 85

@pytest.fixture
def mock_banco():
    mock_db = mock.Mock(spec=BancoDeDados)
    mock_db.buscar.return_value = {"id": 1, "cliente": "João"}
    
    return mock_db


def test_obterPedidoTotal(mock_banco):
    mock_response = [
        {"preco": 10.0, "quantidade": 2},
        {"preco": 5.0, "quantidade": 1},
        {"preco": 20.0, "quantidade": 3}
    ]

    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_response
        
        pedidoTotal = obterPedidoTotal(1, mock_banco)
    
    #(10 * 2) + (5 * 1) + (20 * 3) = 20 + 5 + 60 = 85
    assert pedidoTotal["id"] == 1
    assert pedidoTotal["cliente"] == "João"
    assert pedidoTotal["valorTotal"] == 85
