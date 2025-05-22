class DescritivoMixin:
    def descrever_objetos(self):
        return (f"Produto: {self.nome}, Preço: R${self.preco}")
    def descrever_dicionarios(self):
        return (f"Produto: {self['nome']}, Preço: R${self['preco']}")
