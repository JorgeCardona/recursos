# pip install snowflake-connector-python
from IDataBaseConnector import IDataBaseConnector
import snowflake.connector

class SnowflakeConnector(IDataBaseConnector):
    
    def __init__(self, **connection_params):
        self.user = connection_params.get('user')
        self.password = connection_params.get('password')
        self.account = connection_params.get('account')
        self.warehouse = connection_params.get('warehouse')
        self.database = connection_params.get('database')
        self.schema = connection_params.get('schema')
        self.connection = None
        self.cursor = None
    
    def initialize_connection(self):
        try:
            self.connection = snowflake.connector.connect(
                user=self.user,
                password=self.password,
                account=self.account,
                warehouse=self.warehouse,
                database=self.database,
                schema=self.schema
            )
            self.cursor = self.connection.cursor()
            return self.connection

        except snowflake.connector.errors.DatabaseError as error:
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
                
        except snowflake.connector.errors.DatabaseError as error:
            print(f"Error closing the connection to the database: {error}")
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
