from imports import *


class Preco(BaseClass):
    def __init__(self, preco_id=None, cache_preco=None, id_artista=None, id_tipo_evento=None):
        self.id = preco_id
        self.cache = cache_preco
        self.artista_id = id_artista
        self.tipo_evento_id = id_tipo_evento

    def __str__(self):
        return f"[{self.id}, {self.cache}, {self.artista_id}, {self.tipo_evento_id}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, cachê, artista_id, tipo_evento_id FROM precos WHERE id = {id}")

        return Preco(result[0], result[1], result[2], result[3])
