#pip install mysql-connector-python

from IDataBaseConnector import IDataBaseConnector
import mysql.connector

class MySQLConnector(IDataBaseConnector):
    
    def __init__(self, **connection_params):
        self.user = connection_params.get('user')
        self.password = connection_params.get('password')
        self.host = connection_params.get('host')
        self.port = connection_params.get('port', 3306)
        self.database = connection_params.get('database')
        self.connection = None
        self.cursor = None
    
    def initialize_connection(self):
        try:
            self.connection = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return self.connection

        except mysql.connector.Error as error:
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
                
        except mysql.connector.Error as error:
            print(f"Error closing the connection to the database: {error}")
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Proporciona los parámetros al constructor
    connection_params_mysql = {
        'user': 'your_user',
        'password': 'your_password',
        'host': 'your_host',
        'port': 3306,  # Puerto por defecto para MySQL
        'database': 'your_database'
    }
    mysql_connector = MySQLConnector(**connection_params_mysql)
    connection_mysql = mysql_connector.initialize_connection()
    # Realizar operaciones con la conexión utilizando mysql_connector.connection y mysql_connector.cursor...
    
    # Cerrar la conexión cuando sea necesario
    mysql_connector.close_connection()
