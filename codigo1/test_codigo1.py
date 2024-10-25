from codigo1 import *

def test_email_valido():
    assert email_valido("teste@exemplo.com") == True
    assert email_valido("teste@exemplo") == False
    assert email_valido("test@.com") == False
    assert email_valido("teste@exemplo.com.br") == True
    assert email_valido("") == False

def test_eh_par():
    assert eh_par(2) == True
    assert eh_par(3) == False
    assert eh_par(0) == True
    assert eh_par(-2) == True
    assert eh_par(-3) == False

def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(3) == 6
    
def test_quadrado():
    assert quadrado(3) == 9
    assert quadrado(-3) == 9
    assert quadrado(0) == 0

def test_eh_positivo():
    assert eh_positivo(5) == True
    assert eh_positivo(0) == False
    assert eh_positivo(-5) == False

def test_verificar_maioridade():
    assert verificar_maioridade(18) == 'maior de idade'
    assert verificar_maioridade(17) == 'menor de idade'
    assert verificar_maioridade(30) == 'maior de idade'

def test_classificar_temperatura():
    assert classificar_temperatura(-5) == 'frio'
    assert classificar_temperatura(10) == 'moderado'
    assert classificar_temperatura(30) == 'quente'

def test_avaliar_nota():
    assert avaliar_nota(8) == 'aprovado'
    assert avaliar_nota(6) == 'recuperacao'
    assert avaliar_nota(4) == 'reprovado'

def test_pode_votar():
    assert pode_votar(20) == 'voto obrigatório'
    assert pode_votar(17) == 'voto facultativo'
    assert pode_votar(15) == 'não pode votar'

def test_avaliar_produto():
    assert avaliar_produto(5) == 'excelente'
    assert avaliar_produto(4) == 'bom'
    assert avaliar_produto(3) == 'regular'
    assert avaliar_produto(2) == 'ruim'
    assert avaliar_produto(1) == 'péssimo'
    assert avaliar_produto(0) == 'valor inválido'
