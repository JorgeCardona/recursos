#pip install pyodbc

from IDataBaseConnector import IDataBaseConnector
import pyodbc

class SQLServerConnector(IDataBaseConnector):
    
    def __init__(self, **connection_params):
        self.server = connection_params.get('server')
        self.database = connection_params.get('database')
        self.user = connection_params.get('user')
        self.password = connection_params.get('password')
        self.connection = None
        self.cursor = None
    
    def initialize_connection(self):
        try:
            connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.user};PWD={self.password};"
            self.connection = pyodbc.connect(connection_string)
            self.cursor = self.connection.cursor()
            return self.connection

        except pyodbc.Error as error:
            print(f"Error connecting to the database: {error}")
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()

    def close_connection(self):
        try:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                
        except pyodbc.Error as error:
            print(f"Error closing the connection to the database: {error}")
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Proporciona los parámetros al constructor
    connection_params_sql_server = {
        'server': 'your_server',
        'database': 'your_database',
        'user': 'your_user',
        'password': 'your_password'
    }
    sql_server_connector = SQLServerConnector(**connection_params_sql_server)
    connection_sql_server = sql_server_connector.initialize_connection()
    # Realizar operaciones con la conexión utilizando sql_server_connector.connection y sql_server_connector.cursor...
    
    # Cerrar la conexión cuando sea necesario
    sql_server_connector.close_connection()