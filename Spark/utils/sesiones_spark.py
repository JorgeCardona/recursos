def crear_sesion_spark(app_name="Practica PySpark"):
    from pyspark.sql import SparkSession

    spark_sesion = SparkSession  \
                    .builder  \
                    .master("local[*]")  \
                    .appName(app_name) \
                    .config('spark.ui.port','4040')  \
                    .getOrCreate()

    return spark_sesion

def crear_spark_context_de_spark_sesion(app_name="Practica PySpark"):

    spark_sesion = crear_sesion_spark(app_name=app_name)
    return spark_sesion.sparkContext


def crear_nueva_sesion_spark(objeto_de_sesion):

    return objeto_de_sesion.newSession()


def crear_spark_context():

    from pyspark import SparkContext

    # Crear el objeto SparkContext
    sc = SparkContext()

    return sc

def cerrar_sesion_context(objeto_de_sesion):

    objeto_de_sesion.close()

    print('Objeto de Sesion Exitosamente')