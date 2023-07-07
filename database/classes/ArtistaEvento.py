from imports import *


class ArtistaEvento(BaseClass):
    def __init__(self, artista_evento_id=None, id_artista=None, id_evento=None):
        self.id = artista_evento_id
        self.artista_id = id_artista
        self.evento_id = id_evento

    def __str__(self):
        return f"[{self.id}, {self.artista_id}, {self.evento_id}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, artista_id, evento_id FROM artistas_eventos WHERE id = {id}")

        return ArtistaEvento(result[0], result[1], result[2])
