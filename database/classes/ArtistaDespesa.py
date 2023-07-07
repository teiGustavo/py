from imports import *


class ArtistaDespesa(BaseClass):
    def __init__(self, despesa_id=None, hospedagem_despesa=None, id_preco=None, id_despesa=None, cache_despesa=None):
        self.id = despesa_id
        self.hospedagem = hospedagem_despesa
        self.preco_id = id_preco
        self.despesa_id = id_despesa
        self.cache = cache_despesa

    def __str__(self):
        return f"[{self.id}, {self.hospedagem}, {self.cache}, {self.preco_id}, {self.despesa_id}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, hospedagem, preco_id, despesa_id, cachê "
                                      f"FROM artistas_despesas WHERE id = {id}")

        return ArtistaDespesa(result[0], result[1], result[2], result[3], result[4])
