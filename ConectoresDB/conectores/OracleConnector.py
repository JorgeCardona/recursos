#pip install cx_Oracle
from interfaces import IDataBaseSQLConnector
import cx_Oracle

class OracleConnector(IDataBaseSQLConnector):
    
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

    def get_connection_url(self, dialect="oracle+cx_oracle"):
        return f"{dialect}://{self.user}:{self.password}@{self.dsn}"