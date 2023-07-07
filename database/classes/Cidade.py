from imports import *


class Cidade(BaseClass):
    def __init__(self, cidade_id=None, nome_cidade=None, id_estado=None):
        self.id = cidade_id
        self.nome = nome_cidade
        self.estado_id = id_estado

    def __str__(self):
        return f"[{self.id}, {self.nome}, {self.estado_id}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, nome_cidade, estado_id FROM cidades WHERE id = {id}")

        return Cidade(result[0], f"{result[1]}", result[2])
