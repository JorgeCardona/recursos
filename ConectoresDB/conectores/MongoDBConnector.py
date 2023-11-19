#pip install pymongo
from interfaces import IDataBaseNoSQLConnector
from pymongo import MongoClient

class MongoDBConnector(IDataBaseNoSQLConnector):
    
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

    def get_connection_url(self):
        if self.user and self.password:
            return f"mongodb+srv://{self.user}:{self.password}@{self.host}/{self.database}"
        else:
            return f"mongodb+srv://{self.host}/{self.database}"