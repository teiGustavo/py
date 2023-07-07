from imports import *


manager = QueryManager()
# manager.read_and_print_query("SELECT * FROM cidades", ["ID", "Cidade", "Estado"])

estado = Estado().findById(1)
cidade = Cidade().findById(1)
artista = Artista().findById(1)
tipo_evento = TipoEvento().findById(1)
preco = Preco().findById(1)
evento = Evento().findById(1)
artista_evento = ArtistaEvento().findById(1)
despesa = Despesa().findById(1)
artista_despesa = ArtistaDespesa().findById(1)
receita = Receita().findById(1)
lucro = Lucro().findById(1)

print(estado)
print(cidade)
print(artista)
print(tipo_evento)
print(preco)
print(evento)
print(artista_evento)
print(despesa)
print(artista_despesa)
print(receita)
print(lucro)
