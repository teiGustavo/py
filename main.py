from imports import *


manager = QueryManager()
# manager.read_and_print_query("SELECT * FROM cidades", ["ID", "Cidade", "Estado"])

mg = Estado().from_db(1)


