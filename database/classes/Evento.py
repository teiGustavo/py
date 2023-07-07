from imports import *


class Evento(BaseClass):
    def __init__(self, evento_id=None, data_evento=None, localizacao_evento=None, valor_ingresso_evento=None,
                 publico_maximo_evento=None, id_tipo_evento=None, id_cidade=None, publico_presente_evento=None):
        self.id = evento_id
        self.data = data_evento
        self.localizacao = localizacao_evento
        self.valor_ingresso = valor_ingresso_evento
        self.publico_maximo = publico_maximo_evento
        self.tipo_evento_id = id_tipo_evento
        self.cidade_id = id_cidade
        self.publico_presente = publico_presente_evento

    def __str__(self):
        return f"[{self.id}, {self.data}, {self.localizacao}, {self.valor_ingresso}, {self.publico_maximo}," \
               f"{self.publico_presente}, {self.tipo_evento_id}, {self.cidade_id}]"

    @classmethod
    def findById(cls, id: int):
        manager = QueryManager()
        result = manager.select_query(f"SELECT id, data_evento, localizacao, valor_ingresso, "
                                      f"publico_maximo, tipo_evento_id, cidade_id, publico_presente "
                                      f"FROM eventos WHERE id = {id}")

        return Evento(result[0], f"{result[1]}", f"{result[2]}", result[3], result[4], result[5], result[6], result[7])
