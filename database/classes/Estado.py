from imports import *


class Estado:
    def __init__(self, estado_id=None, nome_estado=None):
        self.id = estado_id
        self.nome = nome_estado

    @classmethod
    def from_db(cls, id_estado: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, nome_estado FROM estados WHERE id = {id_estado}")

        return Estado(result[0], f"{result[1]}")
