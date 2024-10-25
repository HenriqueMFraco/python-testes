import math

# Função para Soma
def soma(a, b):
    return a + b

# Função para Subtração
def subtrai(a, b):
    return a - b

# Função para Multiplicação
def multiplica(a, b):
    return a * b

# Função para Divisão
def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero não permitida."
    return a / b

# Função para Calcular a Área de um Círculo
def area_circulo(raio):
    if raio < 0:
        return "Erro: o raio não pode ser negativo."
    return math.pi * (raio ** 2)

# Função para Calcular a Área de um Retângulo
def area_retangulo(largura, altura):
    if largura < 0 or altura < 0:
        return "Erro: largura e altura devem ser não-negativos."
    return largura * altura