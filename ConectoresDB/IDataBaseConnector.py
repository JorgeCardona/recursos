from abc import ABC, abstractmethod

class IDataBaseConnector(ABC):
    
    @abstractmethod
    def initialize_connection(self):
        pass
    
    @abstractmethod
    def close_connection(self):
        pass