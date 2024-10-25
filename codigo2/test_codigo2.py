from codigo2 import *

import math

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(-1, -1) == -2

def test_subtrai():
    assert subtrai(5, 3) == 2
    assert subtrai(3, 5) == -2
    assert subtrai(0, 0) == 0

def test_multiplica():
    assert multiplica(2, 3) == 6
    assert multiplica(-1, 1) == -1
    assert multiplica(0, 10) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 0) == "Erro: divisão por zero não permitida."
    assert divide(-6, 2) == -3

def test_area_circulo():
    assert area_circulo(3) == math.pi * 9
    assert area_circulo(-1) == "Erro: o raio não pode ser negativo."
    assert area_circulo(0) == 0

def test_area_retangulo():
    assert area_retangulo(4, 5) == 20
    assert area_retangulo(-1, 5) == "Erro: largura e altura devem ser não-negativos."
    assert area_retangulo(4, -2) == "Erro: largura e altura devem ser não-negativos."
    assert area_retangulo(0, 5) == 0
