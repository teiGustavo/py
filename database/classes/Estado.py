from imports import *


class Estado(BaseClass):
    def __init__(self, estado_id=None, nome_estado=None):
        self.id = estado_id
        self.nome = nome_estado

    def __str__(self):
        return f"[{self.id}, {self.nome}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, nome_estado FROM estados WHERE id = {id}")

        return Estado(result[0], f"{result[1]}")
