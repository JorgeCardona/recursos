#pip install pymssql
from interfaces import IDataBaseSQLConnector
import pymssql

class SQLServerConnector(IDataBaseSQLConnector):
    
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

    def get_connection_url(self, dialect="mssql+pymssql"):
        return f"{dialect}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"