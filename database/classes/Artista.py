from imports import *


class Artista(BaseClass):
    def __init__(self, artista_id=None, nome_artista=None, telefone_artista=None,
                 email_artista=None, webpage_artista=None):
        self.id = artista_id
        self.nome = nome_artista
        self.telefone = telefone_artista
        self.email = email_artista
        self.webpage = webpage_artista

    def __str__(self):
        return f"[{self.id}, {self.nome}, {self.telefone}, {self.email}, {self.webpage}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, nome, telefone, email, pagina_web FROM artistas WHERE id = {id}")

        return Artista(result[0], f"{result[1]}", f"{result[2]}", f"{result[3]}", f"{result[4]}")
