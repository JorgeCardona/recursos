#pip install psycopg2
from interfaces import IDataBaseSQLConnector
import psycopg2

class PostgreSQLConnector(IDataBaseSQLConnector):
    
    def __init__(self, **connection_params):
        self.user = connection_params.get('user')
        self.password = connection_params.get('password')
        self.host = connection_params.get('host')
        self.port = connection_params.get('port', 5432)
        self.database = connection_params.get('database')
        self.connection = None
        self.cursor = None
    
    def initialize_connection(self):
        try:
            self.connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return self.connection
        except psycopg2.Error as error:
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
        except psycopg2.Error as error:
            print(f"Error closing the connection to the database: {error}")
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
    
    def get_connection_url(self, dialect="postgresql+psycopg2"):
        return f"{dialect}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"