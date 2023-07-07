from imports import *


class TipoEvento(BaseClass):
    def __init__(self, tipo_evento_id=None, tipo_evento=None):
        self.id = tipo_evento_id
        self.tipo = tipo_evento

    def __str__(self):
        return f"[{self.id}, {self.tipo}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, tipo FROM tipo_eventos WHERE id = {id}")

        return TipoEvento(result[0], f"{result[1]}")
