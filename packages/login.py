from packages.administrador import Administrador
from packages.cliente import Cliente
from packages.bancodedadosjson import DataRecord
from packages.cinema import Cinema

class Login:
    def __init__(self):
        self.banco_de_usuarios = DataRecord("cliente.json")
        self.banco_de_administradores = DataRecord("administrador.json")


    def menu(self):
        nao_logado = True


        while nao_logado:
            print("\n--- MENU ---")
            print("1 - Administrador")
            print("2 - Cliente")
            print("3 - Sair")
            escolha = input("Que opção você deseja escolher? ")

            if escolha == "1":
                print("Você escolheu opção 1; Bem-vindo Administrador!")
                nome = input("Digite Nome: ")
                cpf = input("Digite CPF: ")
                carteirinha = input("Digite número da carteirinha: ")
                admin = Administrador(nome, cpf, carteirinha)
                if self.banco_de_administradores.checar_carteirinha(admin):
                    print("Login efetuado.")
                    nao_logado = False
                    self.sessao_user= Cinema(admin)
                else:
                    print("dados incorretos")



            elif escolha == "2":
                print("Você escolheu opção 2; Bem-vindo Cliente!") 
                nome = input("Digite Nome: ")
                cpf = input("Digite CPF: ")
                cliente = Cliente(nome, cpf)
                self.banco_de_usuarios.add(cliente)
                print("Cliente salvo com sucesso!\n")
                nao_logado = False 
                self.sessao_user= Cinema(cliente)


            elif escolha == "3":
                print("Saindo do sistema...")
                nao_logado = False
            else:
                print("Opção inválida. Tente novamente.")
