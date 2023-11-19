from interfaces import IDataBaseSQLConnector, IDataBaseNoSQLConnector
from abc import ABC

class ConnectionFactory:
    
    def __init__(self, connector, connection_params):
        if not self._is_valid_connector(connector):
            raise TypeError("La clase del conector debe heredar de IDataBaseSQLConnector o IDataBaseNoSQLConnector")
        
        self.connector_class = connector
        self.connection_params = connection_params
        self.connection = None

    def _is_valid_connector(self, connector):
        return (
            issubclass(connector, IDataBaseSQLConnector) or
            issubclass(connector, IDataBaseNoSQLConnector)
        )

    def create_instance(self):
        return self.connector_class(connection_params=self.connection_params)

    def initialize_connection(self):
        try:
            self.connection = self.create_instance().initialize_connection()
            return self.connection
        except (ConnectionError, DatabaseError) as error:
            print(f"Error creating connection: {error}")
            return None


class SingletonFactoryConnection:
    _instances = {}

    @classmethod
    def get_instance(cls, connector, connection_params):
        key = connector.__name__
        
        if key not in cls._instances:
            print(f"Nueva instancia creada para {key}")
            cls._instances[key] = ConnectionFactory(connector, connection_params)
        else:
            print(f"La instancia para {key} ya existía, reutilizando...")

        return cls._instances[key]