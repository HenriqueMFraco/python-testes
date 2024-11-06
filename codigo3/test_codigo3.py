from codigo3 import *
import pytest
import requests 

# def test_soma(lista_doida):
#     assert sum(lista_doida) == 21

# def test_tamanho(lista_doida):
#     assert len(lista_doida) == 6

# def test_dobro(soma_dobro):
#     numeros = [40] 
#     assert soma_dobro(numeros) == 80

def test_acordar_cedo():
    assert acordar_cedo(5) != 1
    assert acordar_cedo(6) == "Você é um guerreiro"
    assert acordar_cedo(7) == "Tente novamente amanhã"
    assert acordar_cedo(8) == "Tente novamente amanhã"

def test_tempo_exercicio():
    assert tempo_exercicio(5, 3) == 4 
    assert tempo_exercicio(5, 2) is None 
    assert tempo_exercicio(10, 4) == 9  
    assert tempo_exercicio(0, 1) is None 

def test_tem_exercicio():
    assert tem_exercicio("Futebol") is True
    assert tem_exercicio("Descanso") is False
    assert tem_exercicio("Caminhada") is True
    assert tem_exercicio("Nada") is True
