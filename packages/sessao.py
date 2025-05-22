from packages.filme import Filme
from packages.cliente import Cliente
from packages.bancodedadosjson import DataRecord



class Sessao:
    def __init__(self, horario, filme: Filme):
        self.horario = horario
        self.filme = filme   

    def __str__(self):
        return (f"Sessão:"
                f"Filme {self.filme.titulo};"
                f"Horário: {self.horario};")
    def to_dict(self):
        return { 
            "horario": self.horario,
            "filme": self.filme.titulo
        }
