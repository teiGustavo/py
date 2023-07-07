from imports import *


class Receita(BaseClass):
    def __init__(self, receita_id=None, evento_id=None, renda_receita=None):
        self.id = receita_id
        self.evento_id = evento_id
        self.renda = renda_receita

    def __str__(self):
        return f"[{self.id}, {self.evento_id}, {self.renda}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, evento_id, renda FROM receitas WHERE id = {id}")

        return Receita(result[0], f"{result[1]}", result[2])
