from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.permissao = bool

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"
    def get_permissao(self):
        return self.permissao
