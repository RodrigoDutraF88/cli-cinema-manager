from packages.pessoa import Pessoa
class Administrador(Pessoa):
    def __init__(self, nome, cpf, carteirinha):
        super().__init__(nome, cpf)
        self.nome = nome
        self.cpf = cpf
        self.carteirinha = carteirinha
        self.permissao = True

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "carteirinha": self.carteirinha
        }