class Filme:
    def __init__(self, titulo, duracao, genero):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero

    def __str__(self):
        return (f"Filme: {self.titulo} ;"
                f"Gênero: {self.genero} ;"
                f"Tempo de filme: {self.duracao};")
