#pip install pymongo

from IDataBaseConnector import IDataBaseConnector
from abc import ABC, abstractmethod
from pymongo import MongoClient

class MongoDBConnector(IDataBaseConnector):
    
    def __init__(self, **connection_params):
        self.host = connection_params.get('host')
        self.port = connection_params.get('port', 27017)
        self.user = connection_params.get('user')
        self.password = connection_params.get('password')
        self.database = connection_params.get('database')
        self.connection = None
        self.cursor = None
    
    def initialize_connection(self):
        try:
            # Si tu MongoDB no requiere autenticación, puedes omitir los parámetros de usuario y contraseña
            if self.user and self.password:
                connection_string = f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            else:
                connection_string = f"mongodb://{self.host}:{self.port}/{self.database}"

            self.connection = MongoClient(connection_string)
            self.cursor = self.connection[self.database]
            return self.connection

        except Exception as error:
            print(f"Error connecting to MongoDB: {error}")
            if self.connection is not None:
                self.connection.close()

    def close_connection(self):
        try:
            if self.connection is not None:
                self.connection.close()
                
        except Exception as error:
            print(f"Error closing the connection to MongoDB: {error}")

# Ejemplo de uso
if __name__ == "__main__":
    # Proporciona los parámetros al constructor
    connection_params_mongodb = {
        'host': 'your_host',
        'port': 27017,  # Puerto por defecto para MongoDB
        'user': 'your_user',
        'password': 'your_password',
        'database': 'your_database'
    }
    mongodb_connector = MongoDBConnector(**connection_params_mongodb)
    connection_mongodb = mongodb_connector.initialize_connection()
    # Realizar operaciones con la conexión utilizando mongodb_connector.connection y mongodb_connector.cursor...
    
    # Cerrar la conexión cuando sea necesario
    mongodb_connector.close_connection()