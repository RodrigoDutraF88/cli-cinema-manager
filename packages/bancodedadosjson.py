import json
import os

class DataRecord:
    def __init__(self, filename):
        self.__filename = "packages/db/" +  filename
        self.__models = []
        self.data = self.read()

    def save(self):
        try:
            with open(self.__filename, "w", encoding="utf-8") as fjson:
                json.dump(self.__models, fjson, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")


    def read(self):
        try:
            with open(self.__filename, "r", encoding="utf-8") as fjson:
                self.__models = json.load(fjson)
        except:
            print(f"O arquivo {self.__filename} não existe!")
            self.__models = []

    def add(self, item):
        self.__models.append(vars(item))
        self.save()

    def get_models(self):
        return self.__models
    
    def atualizar_usuario(self, novousuario): #falta fazer um jeito de ter o imput desse novousuario la na opcao 5
        for i in range(len(self.__models)):
            if self.__models[i]['cpf'] == novousuario.cpf:
                self.__models[i] = vars(novousuario)
        self.save()

    def checar_carteirinha(self, usuarioadm): ## checar se no adm.json o usuario tema senha123, dps em loguin usa essa funcao
        for i in range(len(self.__models)): #esse self models se refere a qualquer dos arquiv json q ta sendo trabalhado ne 
            if self.__models[i]['carteirinha'] == usuarioadm.carteirinha and self.__models[i]['cpf'] == usuarioadm.cpf:
                return True
            else:
                return False
            
    def remover_item(self, item):
        for i in range(len(self.__models)):
            if self.__models[i]['nome'] == item.nome:
                posicao = i
                break
        self.__models.pop(i)
        self.save()
            
        
        


