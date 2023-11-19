# pip install sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from concurrent.futures import ThreadPoolExecutor
from interfaces import IDataBaseSQLConnector, TuTabla
from abc import ABC

# Clase para manejar la creación de instancias singleton
class SingletonFactory:
    _instances = {}

    @classmethod
    def get_instance(cls, connector, connection_params):
        if not issubclass(connector, IDataBaseSQLConnector):
            raise TypeError("La clase del conector debe heredar de IDataBaseSQLConnector")

        key = connector.__name__

        if key not in cls._instances:
            print(f"Nueva instancia creada para {key}")
            cls._instances[key] = connector(connection_params=connection_params)
        else:
            print(f"La instancia para {key} ya existía, reutilizando...")

        return cls._instances[key]

# Clase para inicializar la conexión y crear sesiones
class ConnectionInitializer:
    def __init__(self, connector):
        self.connector = connector
        self.session = None

    def create_sqlalchemy_session(self):
        try:
            connection_url = self.connector.get_connection_url()
            engine = create_engine(connection_url)
            Session = sessionmaker(bind=engine)
            self.session = Session()
            return self.session
        except Exception as error:
            print(f"Error creating session: {error}")
            return None

# Clase para procesar datos en lotes
class BatchProcessor:
    @staticmethod
    def process_batch(batch):
        # Implementa la lógica de procesamiento del lote
        # Aquí deberías agregar la lógica específica de procesamiento del lote
        pass

    @staticmethod
    def process_batches_in_parallel(results, process_function, max_workers=None, **kwargs):
        try:
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Procesa los lotes en paralelo
                futures = [executor.submit(process_function, batch, **kwargs) for batch in results]

                # Espera a que todas las tareas se completen
                for future in futures:
                    future.result()
        except Exception as error:
            print(f"Error processing batches in parallel: {error}")

# Clase que coordina las acciones usando las clases anteriores
class DataProcessor:
    def __init__(self, connector, connection_params):
        self.singleton_factory = SingletonFactory()
        self.connection_initializer = ConnectionInitializer
        self.batch_processor = BatchProcessor()

        # Crear una instancia de SQLAlchemySessionSingletonFactoryConnection para MySQLConnector
        self.sqlalchemy_instance = self.singleton_factory.get_instance(connector, connection_params)

    def process_data_in_batches(self, batch_size, columna, valor, max_workers=None):
        try:
            self.connection_initializer.create_sqlalchemy_session()

            # Crea la consulta filtrada por columna y valor
            query = self.connection_initializer.session.query(TuTabla).filter(getattr(TuTabla, columna) == valor)

            # Lista para almacenar los resultados de la consulta
            results = list(query.yield_per(batch_size))

            # Procesa los lotes en paralelo
            self.batch_processor.process_batches_in_parallel(
                results, process_function=self.batch_processor.process_batch, max_workers=max_workers
            )

            # Commit final para asegurar que todas las transacciones se apliquen
            self.connection_initializer.session.commit()
        except Exception as error:
            print(f"Error processing data in batches: {error}")
        finally:
            # Cierra la sesión después de usarla
            if self.connection_initializer.session:
                self.connection_initializer.session.close()

# Uso de la clase DataProcessor con especificación de max_workers
data_processor = DataProcessor(MySQLConnector, {"user": "usuario", "password": "contrasena", "host": "localhost", "port": 3306, "database": "mydb"})

# Procesa datos en lotes con un máximo de 4 trabajadores simultáneos
data_processor.process_data_in_batches(100, "nombre", "Ejemplo", max_workers=4)
