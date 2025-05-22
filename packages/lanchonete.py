from packages.produto import Produto
from packages.bancodedadosjson import DataRecord



class Lanchonete:
    def __init__(self, nome):
        self.nome = nome
        self.cardapio = []


    def adicionar_ao_cardapio(self, produto: Produto):
        self.cardapio.append(produto)
  #      self.banco_de_dados_lanchonete.add(produto.__dict__) #acho que nao eh p ta aqui
        print(f"O item: {produto.nome}, de preço {produto.preco} foi adicionado ao Cardápio.")


