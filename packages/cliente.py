from packages.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.permissao = False
        self.ingressos = []

    def comprar_ingresso(self, sessao):
        self.ingressos.append((sessao))

    def listar_ingressos(self):
        print(f"\nIngressos de {self.nome}:")
        if not self.ingressos:
            print("Nenhum ingresso foi comprado ainda.")
        for sessao in self.ingressos:
            print(f"Sessão: {sessao} ;")

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf
        } 
             
