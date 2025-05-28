from packages.filme import Filme
from packages.mixins import DescritivoMixin
from packages.sessao import Sessao
from packages.cliente import Cliente
from packages.lanchonete import Lanchonete
from packages.produto import Produto
from packages.bancodedadosjson import DataRecord

class Cinema: 
    def __init__(self, user):
        self.filmes = []
        self.sessoes = []
        self.banco_de_dados_lanche = DataRecord("lanche.json")
        self.banco_de_dados_sessao  = DataRecord("sessao.json")
        self.banco_de_usuarios = DataRecord("cliente.json")

        self.user = user
        self.menu_cinema()

    def adicionar_filme(self, filme):
        if self.user.get_permissao():
            self.filmes.append(filme)
            print(f"Filme '{filme.titulo}' adicionado com sucesso.")

    def adicionar_sessao(self, sessao):
        if self.user.get_permissao():
            self.sessoes.append(sessao)
            self.banco_de_dados_sessao.add(sessao)  
            print("Sessão adicionada e salva com sucesso.")


    def listar_filmes(self):
        print("\nFilmes em Cartaz:")
        for filme in self.filmes:
            print(filme)

    def listar_sessoes(self):
        print("\nSessões Disponíveis:")
        num = 1
        for sessao in self.banco_de_dados_sessao.get_models():
            print(f"{num} - Filme da Sessão: {sessao['filme']},Horário: {sessao['horario']}")
            num += 1



    def __str__(self):
        return (f"Seja bem Vindo(a) ao site do cinema")
    
    def menu_cinema(self):  
        self.logado = True       
        while self.logado:
            print(f"Seja bem Vindo(a) ao site do cinema, {self.user.nome} !")
            opcao = input("Escolha um numero para realizar tal tarefa:\n" 
            "1-Adicionar Filme\n" 
            "2-Adicionar Sessão\n"
            "3-Listar Filmes\n"
            "4-Listar Sessões\n" 
            "5-Comprar Ingresso Para Sessão escolhida\n" 
            "6-Listar Seus ingressos comprados\n" 
            "7-Comprar na Lanchonete\n"
            "8-Adicionar produtos à lanchonete\n" 
            "9-Sair\n")

            if opcao == "1" and self.user.get_permissao():  
                print("Você escolheu Adicionar filme;")
                nome_filme = input("Digite nome do filme:")
                duracao_filme= input("Digite duração do filme:")
                genero_filme= input("Digite gênero do filme:")
                novo_filme = Filme(nome_filme, duracao_filme, genero_filme)
                self.adicionar_filme(novo_filme)

        
            elif opcao == "2" and self.user.get_permissao():
                print("Você escolheu Adicionar Sessão;")
                filme_sessao = input("Digite nome do filme para sessão:")
                horario_sessao = input("Digite o horario da Sessão:")
                filme_obj = next((f for f in self.filmes if f.titulo == filme_sessao), None) 
                if filme_obj:
                    nova_sessao = Sessao(horario_sessao, filme_obj)
                    self.adicionar_sessao(nova_sessao)
                else:
                    print("Filme não encontrado para criar sessão.")
            

            elif opcao == "3":
                print("Você escolheu Listar Filmes;")
                self.listar_filmes()
            

            elif opcao == "4":
                print("Você escolheu Listar Sessões;")
                self.listar_sessoes()
            

            elif opcao == "5" and not self.user.get_permissao():
                print("Você escolheu Comprar Ingresso.")

                self.listar_sessoes()
                sessao_escolhida = input("Escolha uma sessao")
                if int(sessao_escolhida) > len(self.banco_de_dados_sessao.get_models()):
                    print("Escolha sessão valida.")
            
                else:
                    print("Sessão selecionada e comprada!")
                    self.user.comprar_ingresso(self.banco_de_dados_sessao.get_models()[int(sessao_escolhida)-1])
                    self.banco_de_usuarios.atualizar_usuario(self.user)
                
                
            elif opcao == "6":
                print("Você escolheu listar seus ingressos:")
                
                self.user.listar_ingressos() 
            
            
            elif opcao == "7":
                print("Você escolheu Comprar na Lanchonete:") 
                num = 1
                for produtos in self.banco_de_dados_lanche.get_models():
                    print(f"{num} - {DescritivoMixin.descrever_dicionarios(produtos)}") 
                    num += 1
                numero_escolhido = int(input("Digite número do item que deseja comprar:") )
                if numero_escolhido <=len(self.banco_de_dados_lanche.get_models()):
                    lanche_escolhido = self.banco_de_dados_lanche.get_models()[numero_escolhido -1] 
                    lanche_escolhido = Produto(lanche_escolhido['nome'], lanche_escolhido['preco'])
                    self.banco_de_dados_lanche.remover_item(lanche_escolhido)
                    print("Compra efetuada.")

                else: 
                    print("Numero inválido")
                                          
                 
       


            elif opcao == "8" and self.user.get_permissao():
                print("Você escolheu adicionar lanches à lanchonete:")
                nome_lanchenovo= input("Digite nome do lanche adicionado.")
                preco_lanchenovo= input("Digite preço do lanche adicionado.")
                produto_novo = Produto(nome_lanchenovo, preco_lanchenovo)
                self.banco_de_dados_lanche.add(produto_novo)
                print("Lanche adicionado;")
                print(DescritivoMixin.descrever_objetos(produto_novo))


                
            elif opcao == "9":  
                print("Saindo...")
                self.logado = False
                    
            else: 
                print("Opção inválida ou sem permissão.")


      
            



            
            