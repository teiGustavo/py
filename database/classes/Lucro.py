from imports import *


class Lucro(BaseClass):
    def __init__(self, lucro_id=None, evento_id=None, renda_receita=None):
        self.id = lucro_id
        self.evento_id = evento_id
        self.renda = renda_receita

    def __str__(self):
        return f"[{self.id}, {self.evento_id}, {self.renda}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, evento_id, lucro FROM lucros WHERE id = {id}")

        return Lucro(result[0], f"{result[1]}", result[2])
