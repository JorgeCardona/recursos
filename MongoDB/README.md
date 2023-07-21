# PYSPARK CON POSTGRESQL
### https://www.machinelearningplus.com/pyspark/pyspark-connect-to-postgresql/

# PYSPARK CON MONGODB
### https://www.mongodb.com/docs/spark-connector/current/python-api/

# DOCUMENTACION EJEMPLO MONGODB
# https://sparkbyexamples.com/mongodb/mongodb-sql-join-with-examples/?expand_article=1

# TIPOS DE DATOS

| Tipo de Datos            | Descripción                                                                                                                      | Ejemplo                                         |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| String (Cadena)          | Secuencia de caracteres Unicode.                                                                                                 | "Hola", "MongoDB", "123"                        |
| Integer (Entero)         | Número entero de 32 bits.                                                                                                        | 42, -10, 0                                      |
| Double (Flotante)        | Número de punto flotante de 64 bits.                                                                                             | 3.1416, 2.71828                                 |
| Booleano                | Representa un valor verdadero (`true`) o falso (`false`).                                                                       | true, false                                    |
| ObjectId                | Identificador único de un documento en una colección.                                                                           | ObjectId("6158a1f763c35f8d781288c1")           |
| Array                   | Lista ordenada de elementos, donde cada elemento puede ser de cualquier tipo de dato.                                           | [1, 2, 3], ["manzana", "naranja"]               |
| Object (Objeto)         | Documento BSON (similar a un objeto JSON) que contiene pares clave-valor.                                                         | { "nombre": "Juan", "edad": 30 }                |
| Date (Fecha)            | Representa una fecha y hora específica en milisegundos desde el 1 de enero de 1970 (formato UNIX timestamp).                     | ISODate("2023-07-20T12:34:56.789Z")            |
| Timestamp               | Representa un momento en el tiempo con una marca de tiempo y un valor incremental.                                               | Timestamp(1675273200, 1)                       |
| Null                    | Representa un valor nulo o inexistente.                                                                                         | null                                            |
| Decimal128              | Número decimal de 128 bits utilizado para almacenar valores de punto flotante de alta precisión y escala fija.                  | Decimal128("123.456789012345678901234")        |
| Binary (Binario)        | Datos binarios, como imágenes o archivos, codificados en varios formatos (por ejemplo, binario genérico o UUID).                 | BinData(0, "aGVsbG8=")                          |
| RegExp (Expresión Regular) | Patrón de búsqueda utilizado en consultas.                                                                                     | /patrón/                                       |
| Long                    | Número entero de 64 bits.                                                                                                        | NumberLong("123456789012345")                  |
| MinKey                  | Representa el valor mínimo en un índice. Se utiliza para comparar e identificar el valor mínimo en un rango.                      | MinKey                                         |
| MaxKey                  | Representa el valor máximo en un índice. Se utiliza para comparar e identificar el valor máximo en un rango.                      | MaxKey                                         |
| UUID                    | Identificador único universal (Universally Unique Identifier).                                                                 | UUID("f47ac10b-58cc-4372-a567-0e02b2c3d479")     |
| Symbol                  | Representa un tipo de datos que se utiliza para almacenar cadenas cortas y sin estructura.                                       | Symbol("mongodb")                              |
| JavaScript              | Código JavaScript que puede ser evaluado por el motor de JavaScript de MongoDB.                                                 | JavaScript("function() { return 'Hola'; }")    |
| Code with Scope         | Permite almacenar código JavaScript junto con un alcance (conjunto de variables) relacionado.                                   | { code: "function() { return 'Hola'; }", scope: { variable: "valor" } } |
| Decimal128              | Número decimal de 128 bits utilizado para almacenar valores de punto flotante de alta precisión y escala fija.                  | Decimal128("123.456789012345678901234")        |
| MinKey                  | Representa el valor mínimo en un índice y se utiliza para comparar e identificar el valor mínimo en un rango.                    | MinKey                                         |
| MaxKey                  | Representa el valor máximo en un índice y se utiliza para comparar e identificar el valor máximo en un rango.                    | MaxKey                                         |
| RegExp (Expresión Regular) | Patrón de búsqueda utilizado en consultas.                                                                                     | /patrón/                                       |

# ACCEDER A LA CONSOLA DE MONGO DENTRO DE MONGODB COMPASS
<img src="imagenes\00_mongosh.png">


# LISTAR LAS BASES DE DATOS EXISTENTES
```sql
> show dbs
admin    40.00 KiB
config  108.00 KiB
local    40.00 KiB
```
# CREAR UNA BASE DE DATOS

```sql
> use test_mongo
```

# SI NO HAY COLECCIONES NO MUESTRA LA BASE DE DATOS
```sql
test_mongo > show dbs
admin    40.00 KiB
config  108.00 KiB
local    40.00 KiB
```

# CREAR UNA COLECCION
```sql
test_mongo > db.createCollection("vuelos")
{ ok: 1 }
```

# LISTAR LAS BASES DE DATOS EXISTENTES
```sql
> show dbs
admin        40.00 KiB
config      116.00 KiB
local        40.00 KiB
test_mongo    8.00 KiB
```

# VERIFICAR LAS COLECCIONES EXISTENTES
```sql
test_mongo > show collections
vuelos
```

# CONSULTAR TODOS LOS DOCUMENTOS DE UNA COLECCION
```
test_mongo > db.vuelos.find()

```

# ELIMINAR UNA COLECCION
```sql
db.vuelos.drop()
true

test_mongo > show collections

```

# ELIMINAR UNA BASE DE DATOS
```sql
test_mongo > db.dropDatabase()
{ ok: 1, dropped: 'test_mongo'}
```

# VALIDANDO LAS BASES DE DATOS EXISTENTES
```
test_mongo > show databases
admin    40.00 KiB
config  108.00 KiB
local    40.00 KiB
```

# CREAR UNA BASE DE DATOS Y UNA COLECCION USANDO LA INTERFACE
<img src="imagenes\01_crear_data_base.png">

# INSERTAR DATOS EN UNA COLECCION USANDO LA INTERFACE
<img src="imagenes\02_insertar_datos.png">
<img src="imagenes\03_insertar_datos.png">

# CREAR UNA COLECCION NUEVA USANDO LA INTERFACE
<img src="imagenes\04_insertar_datos.png">

# INSERTAR DATOS EN LA COLECCION USANDO LA INTERFACE
<img src="imagenes\05_insertar_datos.png">
<img src="imagenes\06_insertar_datos.png">

# IMPORTAR UN CSV EN MOGONDB
