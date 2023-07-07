from imports import *


class QueryManager:
    def __init__(self):
        self.conn = create_db_connection("localhost", "root", "root", "eventos")
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()

        except Error as err:
            print(f"Error: '{err}'")

    def read_query(self, query):
        try:
            self.cursor.execute(query)
            resultado = self.cursor.fetchall()
            return resultado

        except Error as err:
            print(f"Error: '{err}'")

    def select_query(self, query):
        try:
            self.cursor.execute(query)
            resultado = self.cursor.fetchone()
            return resultado

        except Error as err:
            print(f"Error: '{err}'")

    def read_and_print_query(self, query, columns):
        result_query = self.read_query(query)

        results = []
        for result in result_query:
            results.append(list(result))

        data_frame = pd.DataFrame(results, columns=columns)
        print(data_frame)

