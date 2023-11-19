from abc import ABC, abstractmethod

class IDataBaseSQLConnector(ABC):
    
    @abstractmethod
    def initialize_connection(self):
        pass
    
    @abstractmethod
    def close_connection(self):
        pass
    
    @abstractmethod
    def get_connection_url(self):
        pass