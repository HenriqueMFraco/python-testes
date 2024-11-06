import requests

class BancoDeDados:
    def buscar(self, peidoid):
        # Simula uma consulta ao banco de dados para obter um pedido
        raise NotImplementedError("Consulta real ao banco de dados")

def calcular(peidoid):
    # Simula uma chamada a uma API externa para obter detalhes dos produtos
    resposta = requests.get(f"http://api.loja.com/pedidos/{peidoid}")
    dados_produtos = resposta.json()
    
    # Calcula o valor total com base no preço e quantidade de cada produto
    total = sum(item["preco"] * item["quantidade"] for item in dados_produtos)
    return total

def obterPedidoTotal(peidoid, banco):
    # Busca o pedido no banco de dados
    pedido = banco.buscar(peidoid)
    
    # Calcula o valor total do pedido
    valorTotal = calcular(peidoid)
    
    # Adiciona o valor total ao pedido
    pedido["valorTotal"] = valorTotal
    
    return pedido