import requests
import os

# Asignar valor de parámetro en el notebook desde un widget de texto
def assign_notebook_parameter_value_from_text_widget(widget_config: dict) -> None:
    """
    Crea widgets de texto en Databricks y asigna sus valores a variables de Python en el notebook.

    Esta función itera sobre un diccionario de widgets, creando cada widget de texto en Databricks y almacenando su
    valor en una variable de Python correspondiente al nombre del widget.

    Parámetros:
    - widget_config (dict): Un diccionario donde cada clave es el nombre del widget, y el valor es otro diccionario
                             que contiene 'value' (valor por defecto del widget) y 'label' (etiqueta del widget).
                             Ejemplo:
                             {
                                 'redWineUrl': {'value': 'http://example.com/redWine.csv', 'label': 'URL del Vino Tinto'},
                                 'saveDirectory': {'value': '/path/to/save', 'label': 'Directorio de Guardado' }
                             }

    Nota:
    - Esta función no devuelve ningún valor. Modifica los widgets de Databricks y asigna los valores de los widgets
      a las variables de Python correspondientes en el ámbito del notebook.
    """
    for widget_name, widget_info in widget_config.items():
        # Crear el widget de texto
        dbutils.widgets.text(widget_name, widget_info['value'], widget_info['label'])

    # Imprimir mensaje de éxito después de crear todos los widgets
    print("Proceso completado: Todos los widgets de texto han sido creados y asignados correctamente.")


def remove_assign_notebook_parameter_value_from_widget():
    """
    Elimina todos los widgets en el notebook de Databricks.
    """
    
    dbutils.widgets.removeAll()
    print("Todos los widgets han sido eliminados.")
    

# Función para descargar y guardar los archivos en databricks
def download_dataset_and_store_in_dbfs(url: str, save_path: str) -> None:
    """
    Descarga un archivo desde una URL y lo guarda en el Databricks File System (DBFS).

    Esta función descarga el contenido de un archivo desde una URL dada y lo guarda en una ruta dentro de DBFS.

    Parámetros:
    - url (str): URL desde donde se descargará el archivo.
    - save_path (str): Ruta completa en DBFS donde se guardará el archivo descargado.

    Excepciones:
    - requests.exceptions.RequestException: Si ocurre un error durante la descarga del archivo.
    - Exception: Para cualquier otro error inesperado, como problemas al guardar el archivo en DBFS.

    Ejemplo de uso:
    ```python
    download_dataset_and_store_in_dbfs("https://example.com/file.csv", "/dbfs/tmp/data/file.csv")
    ```

    El archivo será guardado en la ubicación especificada dentro de DBFS.
    """
    try:
        # Descargar el contenido del archivo
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa

        # Usar dbutils.fs.put para guardar el contenido en DBFS
        dbutils.fs.put(save_path, response.text, overwrite=True)

        print(f"Archivo guardado correctamente en {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo desde {url}: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar el archivo en DBFS: {e}")

def delete_file_from_dbfs(file_path):
    """
    Elimina un archivo de DBFS (Databricks File System).
    
    Parámetros:
    file_path (str): La ruta completa del archivo en DBFS.
    
    dbfs:/FileStore/tableswinequality-white.csv
    """
    # Elimina el archivo especificado
    dbutils.fs.rm(file_path, recurse=True)
    
    # Verifica si el archivo ha sido eliminado
    print(f"Archivo {file_path} eliminado.")
    display(dbutils.fs.ls(os.path.dirname(file_path)))

def list_files_in_directory_path(directory_path: str) -> None:
    """
    Lista los archivos dentro de un directorio especificado. Si no hay archivos, imprime un mensaje indicando
    que el directorio está vacío.

    Parámetros:
    - directory_path (str): Ruta completa del directorio cuyo contenido se desea listar.

    Retorno:
    - None: Esta función no retorna ningún valor, solo imprime el contenido del directorio o un mensaje de vacío.
    """
    files = dbutils.fs.ls(directory_path)
    if not files:
        print(f"No hay archivos en el directorio {directory_path}.")
    else:
        print(f"Archivos en el directorio {directory_path}:")
        for file in files:
            print(file.path)

def delete_all_files_in_directory_path(directory_path: str) -> None:
    """
    Elimina todos los archivos dentro de un directorio especificado. Si el directorio está vacío, imprime un mensaje 
    indicando que no hay archivos para eliminar.

    Parámetros:
    - directory_path (str): Ruta completa del directorio cuyo contenido se desea eliminar.

    Retorno:
    - None: Esta función no retorna ningún valor, solo imprime el estado de eliminación de los archivos.
    """
    # Listar todos los archivos en el directorio
    files = dbutils.fs.ls(directory_path)

    if not files:
        print(f"No hay archivos para eliminar en el directorio {directory_path}.\n")
    else:
        # Eliminar cada archivo encontrado
        print(f"Eliminando archivos en el directorio {directory_path}...\n")
        for file in files:
            dbutils.fs.rm(file.path, recurse=True)
            print(f"Archivo eliminado: {file.path}")
        
        print(f"\nTodos los archivos en el directorio {directory_path} han sido eliminados.\n")
        
# FUNCION PARA EJECUTAR LOS QUERIES EN SPARKSQL
def create_database(database_name: str) -> None:
    """
    Crea una base de datos en Databricks si no existe ya.

    Parámetros:
    - database_name (str): Nombre de la base de datos a crear.

    Retorno:
    - None

    Ejemplo de uso:
    ```python
    create_database("nombre_de_la_base_de_datos")
    ```
    """
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    print(f"La base de datos '{database_name}' ha sido creada exitosamente (o ya existía).")


def drop_database(database_name: str) -> None:
    """
    Elimina una base de datos en Databricks si existe.

    Parámetros:
    - database_name (str): Nombre de la base de datos que se desea eliminar.

    Retorno:
    - None

    Nota:
    Esta función elimina la base de datos especificada únicamente si existe. Para eliminar una base de datos que contenga
    tablas u objetos, utiliza la opción CASCADE dentro del comando SQL.

    Ejemplo de uso:
    ```python
    drop_database("nombre_de_la_base_de_datos")
    ```
    """
    spark.sql(f"DROP DATABASE IF EXISTS {database_name} CASCADE")
    print(f"La base de datos '{database_name}' ha sido eliminada exitosamente (si existía).")

def execute_spark_sql_query(query: str):
    """
    Ejecuta una consulta SQL en Spark.

    Parámetros:
    - query (str): Consulta SQL a ejecutar.

    Retorno:
    - pyspark.sql.dataframe.DataFrame o None: 
        - Si la consulta produce un resultado (como SELECT), retorna un DataFrame.
        - Si la consulta no produce un resultado (como UPDATE o DELETE), retorna None.

    Nota:
    La función asume que la consulta SQL está correctamente formada y que se puede ejecutar en el entorno de Spark.
    """
    try:
        print(f"Ejecutando consulta SQL:\n{query}")
        # Ejecutar el query SQL
        result = spark.sql(query)
        
        # Determinar si la consulta devuelve un DataFrame o no
        if result.isStreaming or hasattr(result, "count"):  # Verifica si tiene un resultado tangible
            print(f"La consulta SQL se ejecutó exitosamente. El número de registros obtenidos es: {result.count()}")
            return result
        else:
            print("La consulta SQL se ejecutó exitosamente. No se generó un resultado para mostrar.")
            return None
    except Exception as e:
        print(f"Ocurrió un error al ejecutar la consulta SQL:\n{query}\nError: {e}")
        return None
    
def list_tables_in_database(database_name: str) -> None:
    """
    Lista y muestra todas las tablas en una base de datos específica en Databricks.

    Parámetros:
    - database_name (str): Nombre de la base de datos de la cual se quieren listar las tablas.

    Retorno:
    - None

    Ejemplo de uso:
    ```python
    list_tables_in_database("mi_base_de_datos")
    ```
    """
    tablas = spark.sql(f"SHOW TABLES IN {database_name}")
    display(tablas)

def list_temp_tables(show_global: bool = False) -> "pyspark.sql.dataframe.DataFrame":
    """
    Lista las tablas temporales en la sesión de Spark y las devuelve como un DataFrame de Spark.

    Parámetros:
    - show_global (bool): Si es True, muestra tablas temporales globales (prefijadas con 'global_temp'). 
                          Si es False, muestra las tablas temporales locales de la sesión.

    Retorno:
    - pyspark.sql.dataframe.DataFrame: Un DataFrame con las tablas temporales disponibles.
    """
    try:
        if show_global:
            # Listar tablas temporales globales
            global_temp_tables = [
                (f"global_temp.{table.name}", "Global Temporary")
                for table in spark.catalog.listTables("global_temp")
            ]
        else:
            # Listar tablas temporales locales
            temp_tables = [
                (table.name, "Local Temporary")
                for table in spark.catalog.listTables()
                if table.isTemporary
            ]
        
        # Combinar los resultados y convertirlos a un DataFrame de Spark
        tables = global_temp_tables if show_global else temp_tables
        if tables:
            schema = ["Table", "Type"]
            display(spark.createDataFrame(tables, schema=schema))
        else:
            print("No se encontraron tablas temporales.")
            schema = ["Table", "Type"]
            display(spark.createDataFrame([], schema=schema))
    except Exception as e:
        print(f"Ocurrió un error al listar las tablas temporales: {e}")
        return None
        
# FUNCIONES PARA GUARDAR LOS DATAFRAMES COMOL DELTA Y PARQUET

def standardize_column_names_from_spark_dataframe(spark_dataframe: "pyspark.sql.dataframe.DataFrame") -> "pyspark.sql.dataframe.DataFrame":
    """
    Estandariza los nombres de las columnas de un DataFrame de Spark reemplazando caracteres no alfanuméricos
    por guiones bajos ("_"). Esta transformación ayuda a evitar problemas de formato en el procesamiento de datos.

    Parámetros:
    - spark_dataframe (pyspark.sql.dataframe.DataFrame): DataFrame de Spark con los nombres de columnas a estandarizar.

    Retorno:
    - pyspark.sql.dataframe.DataFrame: Nuevo DataFrame de Spark con los nombres de columnas estandarizados.
    """
    for col_name in spark_dataframe.columns:
        # Reemplazar caracteres no alfanuméricos por "_"
        new_col_name = ''.join([char if char.isalnum() or char == '_' else '_' for char in col_name])
        spark_dataframe = spark_dataframe.withColumnRenamed(col_name, new_col_name)
    
    print(f"Los nombres de las columnas han sido estandarizados exitosamente. Las columnas ahora usan solo caracteres alfanuméricos y guiones bajos.")
    return spark_dataframe


def save_dataframe_as_delta_format(spark_dataframe: "pyspark.sql.dataframe.DataFrame", path: str) -> None:
    """
    Guarda un DataFrame de Spark en formato Delta en una ubicación específica de almacenamiento.

    Parámetros:
    - spark_dataframe (pyspark.sql.dataframe.DataFrame): DataFrame de Spark a guardar.
    - path (str): Ruta en el sistema de archivos donde se guardará el DataFrame en formato Delta.

    Retorno:
    - None

    Nota:
    Esta función sobrescribe cualquier archivo existente en la ruta especificada.
    """
    spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")

    spark_dataframe = standardize_column_names_from_spark_dataframe(spark_dataframe)
    
    spark_dataframe.write.format("delta").mode("overwrite").save(path)
    print(f"El DataFrame ha sido guardado exitosamente en formato Delta en la ruta: {path}")


def save_dataframe_as_delta_table(spark_dataframe: "pyspark.sql.dataframe.DataFrame", database_name: str, table_name: str) -> None:
    """
    Guarda un DataFrame de Spark como una tabla Delta en una base de datos de Databricks.

    Parámetros:
    - spark_dataframe (pyspark.sql.dataframe.DataFrame): DataFrame de Spark a guardar.
    - database_name (str): Nombre de la base de datos donde se creará la tabla.
    - table_name (str): Nombre de la tabla Delta a crear en la base de datos.

    Retorno:
    - None

    Nota:
    Esta función sobrescribe cualquier tabla existente con el mismo nombre en la base de datos especificada.
    """
    spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")

    full_table_name = f"{database_name}.{table_name}"

    spark_dataframe = standardize_column_names_from_spark_dataframe(spark_dataframe)

    spark_dataframe.write.format("delta").mode("overwrite").saveAsTable(full_table_name)
    print(f"El DataFrame ha sido guardado exitosamente como tabla Delta en la base de datos: {database_name}, tabla: {table_name}")


def save_dataframe_as_parquet_format(spark_dataframe: "pyspark.sql.dataframe.DataFrame", path: str) -> None:
    """
    Guarda un DataFrame de Spark en formato Parquet en una ubicación específica de almacenamiento.

    Parámetros:
    - spark_dataframe (pyspark.sql.dataframe.DataFrame): DataFrame de Spark a guardar.
    - path (str): Ruta en el sistema de archivos donde se guardará el DataFrame en formato Parquet.

    Retorno:
    - None

    Nota:
    Esta función sobrescribe cualquier archivo existente en la ruta especificada.
    """
    spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")

    spark_dataframe.write.format("parquet").mode("overwrite").save(path)
    print(f"El DataFrame ha sido guardado exitosamente en formato Parquet en la ruta: {path}")


def save_dataframe_as_parquet_table(spark_dataframe: "pyspark.sql.dataframe.DataFrame", database_name: str, table_name: str) -> None:
    """
    Guarda un DataFrame de Spark como una tabla Parquet en una base de datos de Databricks.

    Parámetros:
    - spark_dataframe (pyspark.sql.dataframe.DataFrame): DataFrame de Spark a guardar.
    - database_name (str): Nombre de la base de datos donde se creará la tabla.
    - table_name (str): Nombre de la tabla Parquet a crear en la base de datos.

    Retorno:
    - None

    Nota:
    Esta función sobrescribe cualquier tabla existente con el mismo nombre en la base de datos especificada.
    """
    spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")

    full_table_name = f"{database_name}.{table_name}"
    spark_dataframe.write.format("parquet").mode("overwrite").saveAsTable(full_table_name)
    print(f"El DataFrame ha sido guardado exitosamente como tabla Parquet en la base de datos: {database_name}, tabla: {table_name}")

def save_dataframe_as_temp_table(spark_dataframe: "pyspark.sql.dataframe.DataFrame", table_name: str) -> None:
    """
    Guarda un DataFrame de Spark como una tabla temporal en Databricks.

    Parámetros:
    - spark_dataframe (pyspark.sql.dataframe.DataFrame): DataFrame de Spark a guardar como tabla temporal.
    - table_name (str): Nombre de la tabla temporal a crear.

    Retorno:
    - None

    Nota:
    Esta función crea o reemplaza una tabla temporal, que existe solo durante la sesión activa de Spark.
    """
    spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")
    
    spark_dataframe.createOrReplaceTempView(table_name)
    print(f"El DataFrame ha sido guardado exitosamente como tabla temporal: {table_name}")

# FUNCION PARA LEER LOS ARCHIVOS DESCARGADOS COMO SPARK DATAFRAMES

def load_data_to_spark_dataframe(file_location: str, file_type: str = "csv", infer_schema: bool = True, 
                           first_row_is_header: bool = True, delimiter: str = ",") -> "DataFrame":
    """
    Carga un archivo en un DataFrame de Spark, con opciones configurables para tipos de archivo, inferencia de esquema,
    encabezado, y delimitador.

    Parámetros:
    - file_location (str): La ubicación del archivo que se desea cargar.
    - file_type (str): El tipo de archivo. Por defecto es 'csv'. Otros valores pueden incluir 'parquet', 'json', etc.
    - infer_schema (bool): Si se debe inferir el esquema automáticamente del archivo. Por defecto es True.
    - first_row_is_header (bool): Si la primera fila debe ser usada como encabezado. Por defecto es True.
    - delimiter (str): El delimitador para los archivos CSV. Por defecto es ','.

    Retorna:
    - DataFrame: El DataFrame cargado con los datos del archivo.
    """
    try:
        # Cargar el archivo en el DataFrame
        df = spark.read.format(file_type) \
            .option("inferSchema", infer_schema) \
            .option("header", first_row_is_header) \
            .option("sep", delimiter) \
            .load(file_location)
        
        print(f"Archivo cargado correctamente desde {file_location}")
        return df
    
    except Exception as e:
        print(f"Error al cargar el archivo desde {file_location}: {e}")
        return None