def email_valido(email):
    """Verifica se um email é válido."""
    return '@' in email and '.' in email


def eh_par(n):
    """Verifica se um número é par."""
    return n % 2 == 0


def fatorial(n):
    """Calcula o fatorial de um número."""
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    if n == 0:
        return 1
    return n * fatorial(n - 1)


def quadrado(n):
    """Retorna o quadrado de um número."""
    return n ** 2


def eh_positivo(n):
    """Verifica se um número é positivo."""
    return n > 0


def verificar_maioridade(idade):
    """Verifica a maioridade de uma pessoa com base na idade."""
    return 'maior de idade' 
    if idade >= 18 else 'menor de idade'


def classificar_temperatura(temp):
    """Classifica a temperatura em frio, moderado ou quente."""
    if temp < 0:
        return 'frio'
    elif 0 <= temp <= 25:
        return 'moderado'
    else:
        return 'quente'


def avaliar_nota(nota):
    """Avalia a nota em aprovado, recuperação ou reprovado."""
    if nota >= 7:
        return 'aprovado'
    elif 5 <= nota < 7:
        return 'recuperacao'
    else:
        return 'reprovado'


def pode_votar(idade):
    """Verifica se uma pessoa pode votar."""
    if idade >= 18:
        return 'voto obrigatório'
    elif 16 <= idade < 18:
        return 'voto facultativo'
    else:
        return 'não pode votar'


def avaliar_produto(estrelas):
    """Avalia um produto com base na quantidade de estrelas."""
    if estrelas == 5:
        return 'excelente'
    elif estrelas == 4:
        return 'bom'
    elif estrelas == 3:
        return 'regular'
    elif estrelas == 2:
        return 'ruim'
    elif estrelas == 1:
        return 'péssimo'
    else:
        return 'valor inválido'

