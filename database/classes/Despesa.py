from imports import *


class Despesa(BaseClass):
    def __init__(self, despesa_id=None, marketing_despesa=None, id_evento=None):
        self.id = despesa_id
        self.marketing = marketing_despesa
        self.evento_id = id_evento

    def __str__(self):
        return f"[{self.id}, {self.marketing}, {self.evento_id}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, marketing, evento_id FROM despesas WHERE id = {id}")

        return Despesa(result[0], result[1], result[2])
