#pip install cx_Oracle

from IDataBaseConnector import IDataBaseConnector
import cx_Oracle

class OracleConnector(IDataBaseConnector):
    
    def __init__(self, **connection_params):
        self.user = connection_params.get('user')
        self.password = connection_params.get('password')
        self.dsn = connection_params.get('dsn')
        self.connection = None
        self.cursor = None
    
    def initialize_connection(self):
        try:
            self.connection = cx_Oracle.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
            )
            self.cursor = self.connection.cursor()
            return self.connection

        except cx_Oracle.Error as error:
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
                
        except cx_Oracle.Error as error:
            print(f"Error closing the connection to the database: {error}")
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Proporciona los parámetros al constructor
    connection_params_oracle = {
        'user': 'your_user',
        'password': 'your_password',
        'dsn': 'your_dsn'
    }
    oracle_connector = OracleConnector(**connection_params_oracle)
    connection_oracle = oracle_connector.initialize_connection()
    # Realizar operaciones con la conexión utilizando oracle_connector.connection y oracle_connector.cursor...
    
    # Cerrar la conexión cuando sea necesario
    oracle_connector.close_connection()