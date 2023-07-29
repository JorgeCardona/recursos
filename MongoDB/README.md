PAQUETE COLLECIONES
```
 # EL MODULO deque EN PYTHON SE PUEDE COMPORTAR COMO COLA O COMO PILA, DEPENDIENDO DE LOS METODOS DE INSERCION O RECUPERACION DE ELEMENTOS A USAR
from collections import deque
queue = deque([9, 8, 1, 2, 3, 4, 5, 6, 7])
print(queue.pop()) # 9, recupera el elemento de la DERECHA de la cola
print(queue.popleft()) # 7, recupera el elemento de la IZQUIERDA de la cola
queue.append(5) # inserta un elemento a la DERECHA de la cola
queue.appendleft(8) # inserta un elemento a la IZQUIERDA de la cola
print(queue.pop()) # 5
print(queue.popleft()) # 8
list(queue) # [8, 1, 2, 3, 4, 5, 6]
```

| Estructura   | Descripción                                            | Aplicación                                                                                           | Implementación                                         | Métodos Disponibles                                                                         | Uso                                | Valor de Retorno                     |
|--------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------------------------|------------------------------------|-------------------------------------|
| namedtuple   | Una tupla con campos con nombre.                       | Ideal para representar registros o datos inmutables con campos específicos.                        | `from collections import namedtuple`<br>`Person = namedtuple('Person', ['name', 'age'])` | `_fields`, `_asdict()`, `_replace()`, `._make()`, `_asdict()`, `._fields`, `.name`, `.age`  | `person = Person('John', 30)`     | `Person(name='John', age=30)`       |
| deque        | Una cola doblemente terminada.                         | Útil para implementar colas y pilas eficientes que requieran inserciones y eliminaciones en ambos extremos. | `from collections import deque`<br>`queue = deque([1, 2, 3, 4])`                   | `append()`, `appendleft()`, `extend()`, `extendleft()`, `pop()`, `popleft()`, `rotate()`    | `queue.append(5)`<br>`queue.popleft()`  | `None`<br>`1`                       |
| ChainMap     | Agrupa múltiples diccionarios como una sola entidad.   | Excelente para combinar múltiples diccionarios y realizar búsquedas en ellos de manera eficiente.         | `from collections import ChainMap`<br>`dict1 = {'a': 1, 'b': 2}`<br>`dict2 = {'c': 3, 'd': 4}`<br>`chain_map = ChainMap(dict1, dict2)`  | `keys()`, `values()`, `items()`, `new_child()`, `parents`, `maps`                           | `chain_map['a']`<br>`chain_map['d']`    | `1`<br>`4`                           |
| Counter      | Cuenta el número de ocurrencias de elementos.          | Útil para contar elementos en una lista o secuencia y realizar análisis de datos.                    | `from collections import Counter`<br>`counter = Counter('abracadabra')`              | `elements()`, `most_common()`, `subtract()`, `update()`, `.items()`, `.keys()`, `.values()`  | `counter['a']`<br>`counter['b']`        | `5`<br>`2`                           |
| defaultdict | Un diccionario con valores predeterminados.            | Ideal para contadores o acumuladores, donde el valor predeterminado es útil para acumular datos.    | `from collections import defaultdict`<br>`default_dict = defaultdict(int)`<br>`default_dict['a'] += 1` | `clear()`, `copy()`, `default_factory`, `get()`, `items()`, `keys()`, `values()`, `update()`   | `default_dict['a']`<br>`default_dict['b']` | `2`<br>`0`                           |



# iniciar jupyter lab en directorio personalizado
```
jupyter lab --note-dir="C:\z Github\recursos\MongoDB"
```

# copiar el conector para conectarse con pyspark
cp postgresql-42.6.0.jar /usr/local/spark/jars

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

# LISTA DE COMANDOS MAS USADOS

Claro, a continuación, agregaré una columna de ejemplo a la tabla con los 50 comandos más utilizados en MongoDB:

| Comando                                   | Descripción                                                                                      | Ejemplo                                                                                                                     |
|-------------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `use NOMBRE_DB`                           | Cambia al contexto de la base de datos `NOMBRE_DB`. Permite trabajar en una base de datos específica. | `use mi_basededatos`                                                                                                       |
| `show databases`  o `show dbs`                                | Muestra una lista de todas las bases de datos disponibles en el servidor.                           | `show dbs`                                                                                                                |
| `show collections`                        | Muestra una lista de todas las colecciones en la base de datos actual.                               | `show collections`                                                                                                        |
| `db.collection.find()`                    | Recupera documentos de la colección `collection` que satisfacen los criterios de consulta especificados. | `db.mis_documentos.find({ campo: "valor" })`                                                                              |
| `db.collection.insertOne()`               | Inserta un nuevo documento en la colección `collection`.                                          | `db.mis_documentos.insertOne({ campo1: "valor1", campo2: "valor2" })`                                                     |
| `db.collection.updateOne()`               | Actualiza un documento en la colección `collection` que cumpla con los criterios de filtro especificados. | `db.mis_documentos.updateOne({ _id: ObjectId("documento_id") }, { $set: { campo: "nuevo_valor" } })`                       |
| `db.collection.deleteOne()`               | Elimina un documento de la colección `collection` que cumpla con los criterios de filtro especificados. | `db.mis_documentos.deleteOne({ campo: "valor" })`                                                                         |
| `db.collection.aggregate()`               | Realiza una agregación en la colección `collection` para realizar operaciones de agregación avanzadas.  | `db.mis_documentos.aggregate([ { $match: { campo: "valor" } }, { $group: { _id: "$campo", total: { $sum: 1 } } } ])`      |
| `db.collection.createIndex()`             | Crea un índice en la colección `collection` para mejorar el rendimiento de las consultas.            | `db.mis_documentos.createIndex({ campo: 1 })`                                                                            |
| `db.collection.drop()`                    | Elimina la colección `collection` y todos sus documentos.                                         | `db.mis_documentos.drop()`                                                                                                |
| `db.dropDatabase()`                       | Elimina la base de datos actual y todas sus colecciones.                                          | `db.dropDatabase()`                                                                                                       |
| `db.collection.countDocuments()`          | Cuenta el número de documentos en la colección `collection`.                                       | `db.mis_documentos.countDocuments()`                                                                                      |
| `db.collection.distinct()`                | Devuelve una lista de valores distintos para un campo específico en la colección `collection`.       | `db.mis_documentos.distinct("campo")`                                                                                     |
| `db.collection.findOne()`                 | Recupera un solo documento de la colección `collection` que cumpla con los criterios de consulta especificados. | `db.mis_documentos.findOne({ campo: "valor" })`                                                                           |
| `db.collection.find().sort()`             | Ordena los resultados de una consulta en la colección `collection` en función de un campo específico. | `db.mis_documentos.find().sort({ campo: 1 })`                                                                            |
| `db.collection.find().limit()`            | Limita el número de documentos devueltos por una consulta en la colección `collection`.            | `db.mis_documentos.find().limit(10)`                                                                                     |
| `db.collection.find().skip()`             | Omite los primeros documentos devueltos por una consulta en la colección `collection`.             | `db.mis_documentos.find().skip(5)`                                                                                        |
| `db.collection.find().project()`          | Proyecta solo los campos específicos de los documentos devueltos por una consulta en la colección `collection`. | `db.mis_documentos.find({}, { campo1: 1, campo2: 1, _id: 0 })`                                                             |
| `db.collection.find().count()`            | Cuenta el número de documentos devueltos por una consulta en la colección `collection`.            | `db.mis_documentos.find().count()`                                                                                        |
| `db.collection.bulkWrite()`               | Realiza múltiples operaciones de escritura en la colección `collection` en una sola solicitud.      | Ver ejemplo en la documentación oficial de MongoDB.                                                                       |
| `db.collection.replaceOne()`              | Reemplaza un documento en la colección `collection` que cumpla con los criterios de filtro especificados. | `db.mis_documentos.replaceOne({ _id: ObjectId("documento_id") }, { campo: "nuevo_valor" })`                              |
| `db.collection.insertMany()`              | Inserta varios documentos en la colección `collection` a la vez.                                   | `db.mis_documentos.insertMany([{ campo1: "valor1" }, { campo2: "valor2" }])`                                              |
| `db.collection.updateMany()`              | Actualiza múltiples documentos en la colección `collection` que cumplan con los criterios de filtro especificados. | `db.mis_documentos.updateMany({ campo: "valor" }, { $set: { campo: "nuevo_valor" } })`                                    |
| `db.collection.deleteMany()`              | Elimina múltiples documentos de la colección `collection` que cumplan con los criterios de filtro especificados. | `db.mis_documentos.deleteMany({ campo: "valor" })`                                                                        |
| `db.collection.distinct().count()`        | Cuenta el número de valores distintos para un campo específico en la colección `collection`.        | `db.mis_documentos.distinct("campo").length`                                                                             |
| `db.collection.find().explain()`          | Proporciona información sobre cómo MongoDB ejecutó una consulta en la colección `collection`.       | `db.mis_documentos.find().explain()`                                                                                     |
| `db.collection.find().hint()`             | Indica a MongoDB qué índice utilizar para una consulta en la colección `collection`.               | `db.mis_documentos.find().hint({ campo: 1 })`                                                                            |
| `db.collection.aggregate().match()`       | Filtra los documentos que cumplan con los criterios de filtro especificados en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $match: { campo: "valor" } } ])`                                                        |
| `db.collection.aggregate().group()`       | Agrupa los documentos en una operación de agregación en la colección `collection`.                  | `db.mis_documentos.aggregate([ { $group: { _id: "$campo", total: { $sum: 1 } } } ])`                                    |
| `db.collection.aggregate().project()`     | Proyecta solo los campos específicos de los documentos en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $project: { campo1: 1, campo2: 1, _id: 0 } } ])`                                       |
| `db.collection.aggregate().sort()`        | Ordena los documentos en una operación de agregación en la colección `collection`.                  | `db.mis_documentos.aggregate([ { $sort: { campo: 1 } } ])`                                                               |
| `db.collection.aggregate().limit()`       | Limita el número de documentos devueltos por una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $limit: 10 } ])`                                                                        |
| `db.collection.aggregate().skip()`        | Omite los primeros documentos devueltos por una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $skip: 5 } ])`                                                                          |
| `db.collection.aggregate().unwind()`      | Descompone un campo de matriz en varios documentos en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $unwind: "$campo" } ])`                                                                 |
| `db.collection.aggregate().lookup()`      | Realiza una operación de unión (join) entre dos colecciones en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $lookup: { from: "otra_coleccion", localField: "campo", foreignField: "campo", as: "resultado" } } ])` |
| `db.collection.aggregate().out()`         | Escribe los resultados de una operación de agregación en otra colección.                            | `db.mis_documentos.aggregate([ { $out: "resultados_agregacion" } ])`                                                     |
| `db.collection.aggregate().facet()`       | Divide los resultados de una operación de agregación en múltiples subconjuntos.                     | `db.mis_documentos.aggregate([ { $facet: { subconjunto1: [ { $match: { campo: "valor1" } } ], subconjunto2: [ { $match: { campo: "valor2" } } ] } } ])` |
| `db.collection.aggregate().bucket()`      | Agrupa los documentos en intervalos específicos en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $bucket: { groupBy: "$campo", boundaries: [0, 100, 200], default: "Otros", output: { "total": { $sum: 1 } } } } ])` |
| `db.collection.aggregate().sortByCount()` | Agrupa los documentos por su valor y devuelve el recuento de cada grupo en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $sortByCount: "$campo" } ])`                                                            |
| `db.collection.aggregate().facet().project()` | Proyecta solo los campos específicos de los subconjuntos en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $facet: { subconjunto1: [ { $match: { campo: "valor1" } } ], subconjunto2: [ { $match: { campo: "valor2" } } ] } }, { $project: { subconjunto1: 1 } } ])` |
| `db.collection.aggregate().unwind().group()` | Agrupa los documentos después de descomponer un campo de matriz en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $unwind: "$campo" }, { $group: { _id: "$campo", total: { $sum: 1 } } } ])` |
| `db.collection.aggregate().lookup().unwind()` | Descompone los documentos después de realizar una operación de unión (join) en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $lookup: { from: "otra_coleccion", localField: "campo", foreignField: "campo", as: "resultado" } }, { $unwind: "$resultado" } ])` |
| `db.collection.aggregate().lookup().unwind().group()` | Agrupa los documentos después de realizar una operación de unión (join) y descomponer un campo de matriz en una operación de agregación en la colección `collection`. | `db.mis_documentos.aggregate([ { $lookup: { from: "otra_coleccion", localField: "campo", foreignField: "campo", as: "resultado" }}])`|


# ACCEDER A LA CONSOLA DE MONGO DENTRO DE MONGODB COMPASS
<img src="imagenes\00_mongosh.png">

# ROLES EN MONGODB

| Rol              | Descripción                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------|
| read             | Permite leer datos en una base de datos o colección.                                             |
| readWrite        | Permite leer y escribir datos en una base de datos o colección.                                 |
| dbAdmin          | Proporciona acceso de administrador a una base de datos. Permite ejecutar comandos de administración y ver algunas estadísticas del servidor. |
| userAdmin        | Permite administrar usuarios y roles en una base de datos.                                       |
| clusterAdmin     | Proporciona acceso de administrador a nivel de clúster. Permite realizar operaciones de administración en todas las bases de datos. |
| backup           | Permite realizar copias de seguridad y restauraciones de las bases de datos.                    |
| restore          | Permite restaurar bases de datos desde copias de seguridad.                                      |
| root             | Proporciona acceso de superusuario que puede realizar cualquier acción en cualquier base de datos. |

# CREAR ROL
`use admin`
```mongodb
db.createRole(
   {
     role: "mongo_test_role",
     privileges: [
       { resource: { cluster: true }, actions: [ "addShard" ] },
       { resource: { db: "mongo_test", collection: "vuelos_1" }, actions: [ "find", "update", "insert", "remove" ] }
     ],
     roles: [
       { role: "read", db: "admin" }
     ]
   },
   { w: "majority" , wtimeout: 5000 }
)
```

# CURSOR
Es una estructura iterable, similar a una lista de diccionarios en python. donde se almacenan los resultados de las consultas.


# LISTAR ROLES
`show roles`

```mongodb
[
  {
    role: 'clusterAdmin',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'dbAdminAnyDatabase',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'readWrite',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'directShardOperations',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'readAnyDatabase',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: '__queryableBackup',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'enableSharding',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'readWriteAnyDatabase',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'backup',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'hostManager',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'root',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'clusterManager',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'dbOwner',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: '__system',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'userAdminAnyDatabase',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'userAdmin',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'restore',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'read',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'clusterMonitor',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    role: 'dbAdmin',
    db: 'admin',
    isBuiltin: true,
    roles: [],
    inheritedRoles: []
  },
  {
    _id: 'admin.mongo_test_role',
    role: 'mongo_test_role',
    db: 'admin',
    roles: [
      {
        role: 'read',
        db: 'admin'
      }
    ],
    isBuiltin: false,
    inheritedRoles: [
      {
        role: 'read',
        db: 'admin'
      }
    ]
  }
]
```
# CREAR UN USUARIO
`use admin`

```mongodb
db.createUser({
   user: "mongodb_admin",
   pwd: "12345678",
   roles: ["root"]
}),
db.createUser({
   user: "mongodb_readWrite",
   pwd: "12345678",
   roles: ["readWrite"]
}),
db.createUser({
   user: "mongodb_backup",
   pwd: "12345678",
   roles: ["backup"]
}),
db.createUser({
   user: "mongodb_restore",
   pwd: "12345678",
   roles: ["restore"]
})

{ ok: 1 }
```

# LISTAR USUARIOS

```
show users
```

```mongodb
[
  {
    _id: 'admin.mongodb_admin',
    userId: UUID("99e462a2-6083-4dc7-a96f-5ccb6ad78469"),
    user: 'mongodb_admin',
    db: 'admin',
    roles: [
      {
        role: 'root',
        db: 'admin'
      }
    ],
    mechanisms: [
      'SCRAM-SHA-1',
      'SCRAM-SHA-256'
    ]
  },
  {
    _id: 'admin.mongodb_backup',
    userId: UUID("f984593d-4a0b-4746-b995-390cc7dd8a02"),
    user: 'mongodb_backup',
    db: 'admin',
    roles: [
      {
        role: 'backup',
        db: 'admin'
      }
    ],
    mechanisms: [
      'SCRAM-SHA-1',
      'SCRAM-SHA-256'
    ]
  },
  {
    _id: 'admin.mongodb_readWrite',
    userId: UUID("794c0f07-090c-4274-ba01-a862e48f5874"),
    user: 'mongodb_readWrite',
    db: 'admin',
    roles: [
      {
        role: 'readWrite',
        db: 'admin'
      }
    ],
    mechanisms: [
      'SCRAM-SHA-1',
      'SCRAM-SHA-256'
    ]
  },
  {
    _id: 'admin.mongodb_restore',
    userId: UUID("aa8c213d-3569-404b-a051-0f7bb8a9ad67"),
    user: 'mongodb_restore',
    db: 'admin',
    roles: [
      {
        role: 'restore',
        db: 'admin'
      }
    ],
    mechanisms: [
      'SCRAM-SHA-1',
      'SCRAM-SHA-256'
    ]
  }
]
```

# LISTAR LAS BASES DE DATOS EXISTENTES
```mongodb
show dbs
```

```sql
admin    40.00 KiB
config  108.00 KiB
local    40.00 KiB
```
# CREAR UNA BASE DE DATOS

```sql
use test_mongo
```

# SI NO HAY COLECCIONES NO MUESTRA LA BASE DE DATOS
`show dbs`

```mongodb
admin    40.00 KiB
config  108.00 KiB
local    40.00 KiB
```

# CREAR UNA COLECCION
```mongodb
db.createCollection("vuelos")
```

```mongodb
{ ok: 1 }
```

# LISTAR LAS BASES DE DATOS EXISTENTES
```mongodb
show dbs
```

```mongodb
admin        40.00 KiB
config      116.00 KiB
local        40.00 KiB
test_mongo    8.00 KiB
```

# VERIFICAR LAS COLECCIONES EXISTENTES

```mongodb
show collections
```

```mongodb
vuelos
```

# ELIMINAR UNA COLECCION
```mongodb
db.vuelos.drop()
```

```mongodb
true
```

# VALIDAR COLECCIONES
```mongodb
show collections
```

```mongodb
```

# ELIMINAR UNA BASE DE DATOS
```mongodb
db.dropDatabase()
```

```mongodb
{ ok: 1, dropped: 'test_mongo'}
```

# VALIDANDO LAS BASES DE DATOS EXISTENTES
```mongodb
show databases
```

```mongodb
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

# VALIDAR EN QUE BASE DE DATOS SE ESTA TRABAJANDO
```mongodb
db
```
```mongodb
test_mongo
```

# ESTADISTICAS DE LA BASE DE DATOS
```mongodb
db.stats()
```

```mongodb
{
  db: 'test_mongo',
  collections: 2,
  views: 0,
  objects: 10000,
  avgObjSize: 474.2158,
  dataSize: 4742158,
  storageSize: 1531904,
  indexes: 2,
  indexSize: 131072,
  totalSize: 1662976,
  scaleFactor: 1,
  fsUsedSize: 487334268928,
  fsTotalSize: 510770802688,
  ok: 1
}
```

# LISTAR LOS CAMPOS DE UNA COLECCION
```mongodb
Object.keys(db.vuelos_1.findOne())
```

```mongodb
[
  '_id',              'id',
  'secure_code',      'airline',
  'departure_city',   'departure_date',
  'arrival_airport',  'arrival_city',
  'arrival_time',     'passenger_name',
  'passenger_gender', 'seat_number',
  'currency',         'departure_gate',
  'flight_status',    'co_pilot_name',
  'aircraft_type',    'fuel_consumption'
]
```

# DECLARAR VARIABLES Y HACER USO DE ELLAS
# LISTAR LOS CAMPOS Y LOS TIPOS DE DATOS DE LOS CAMPOS DE UNA COLECCION
```mongodb
const coleccion = db.getCollection('vuelos_1');

const documento = coleccion.findOne()

# FORMA 1, entries -> contiene clave valor
Object.entries(documento).forEach(([clave, valor]) => {
  print(`${clave}: ${typeof valor}`);
});

# FORMA 2, keys -> contiene solo la clave
Object.keys(documento).forEach((campo) => {
  print(`${campo}: ${typeof documento[campo]}`);
});
```

```mongodb
_id: object
id: number
secure_code: string
airline: string
departure_city: string
departure_date: string
arrival_airport: string
arrival_city: string
arrival_time: string
passenger_name: string
passenger_gender: string
seat_number: string
currency: string
departure_gate: string
flight_status: string
co_pilot_name: string
aircraft_type: string
fuel_consumption: number
```

# VER LOS INDICES DE UNA COLECCION
```mongodb
db.vuelos_1.getIndices()
```

```mongodb
[ { v: 2, key: { _id: 1 }, name: '_id_' } ]
```

# CONSULTAR TODOS LOS DOCUMENTOS DE UNA COLECCION
```mongodb
use test_mongo
```

```mongodb
db.vuelos_1.find()
```

```mongodb
{
  _id: ObjectId("64ba0cea510b21bfe34b54f3"),
  id: 1,
  secure_code: '01H4EEMGMG9VADVF06JZGJJGN0',
  airline: 'EasyFly',
  departure_city: 'Berlin',
  departure_date: '25/12/2022',
  arrival_airport: 'PEI',
  arrival_city: 'Pereira',
  arrival_time: '27/12/2022 14:13',
  passenger_name: 'Nathalie Cardona',
  passenger_gender: 'Female',
  seat_number: 'A1',
  currency: 'EUR',
  departure_gate: 'B2',
  flight_status: 'On Time',
  co_pilot_name: 'Hart Blunkett',
  aircraft_type: 'Embraer E190',
  fuel_consumption: 7916.39
}
{
  _id: ObjectId("64ba0cea510b21bfe34b54f4"),
  id: 2,
  secure_code: '01H4EEMGMYP8GX4GRC4Y2MPYH5',
  airline: 'Delta',
  departure_city: "Les Sables-d'Olonne",
  departure_date: '4/1/2022',
  arrival_airport: 'YHU',
  arrival_city: 'Westport',
  arrival_time: '6/7/2023 06:53',
  passenger_name: 'Willie Childrens',
  passenger_gender: 'Female',
  seat_number: 'B2',
  currency: 'EUR',
  departure_gate: 'A1',
  flight_status: 'Delayed',
  co_pilot_name: 'Leanor Gribbins',
  aircraft_type: 'Airbus A320',
  fuel_consumption: 9666.36
}
...
...
...
```

```sql
db.vuelos_2.find()
```

```mongodb
{
  _id: ObjectId("64bb5eb2a21e5a2e74b36a20"),
  flight_id: 1,
  flight_number: 1978,
  departure_airport: 'CFQ',
  departure_country: 'Germany',
  departure_time: '6/7/2023 04:42',
  arrival_country: 'Colombia',
  arrival_date: '27/12/2022',
  flight_duration: 14.18,
  passenger_age: 0,
  passenger_nationality: 'Colombia',
  ticket_price: 797.24,
  baggage_weight: 43.85,
  arrival_gate: 'E5',
  pilot_name: 'Sunny Few',
  cabin_crew_count: 9,
  aircraft_registration: 'N12345',
  flight_distance: 1400.24
}
{
  _id: ObjectId("64bb5eb2a21e5a2e74b36a21"),
  flight_id: 2,
  flight_number: 2337,
  departure_airport: 'ONG',
  departure_country: 'France',
  departure_time: '6/7/2023 17:31',
  arrival_country: 'New Zealand',
  arrival_date: '23/12/2022',
  flight_duration: 13.54,
  passenger_age: 29,
  passenger_nationality: 'Sweden',
  ticket_price: 383.63,
  baggage_weight: 35.78,
  arrival_gate: 'D4',
  pilot_name: 'Donielle Strut',
  cabin_crew_count: 4,
  aircraft_registration: 'N12345',
  flight_distance: 465.84
}
...
...
...
```














# HACER UN JOIN **lookup** ENTRE 2 COLECCIONES Y TRAER SOLO EL PRIMER DOCUMENTO '$limit: 1'

```mongodb
# Join two collections using $lookup operator
 
db.vuelos_1.aggregate([
   {
      $lookup:
         {
           from: "vuelos_2",
           localField: "id",
           foreignField: "flight_id",
           as: "VueloId"
         }
   },
  {
    $limit: 1
  }
])
```

```mongodb
{
  _id: ObjectId("64ba0cea510b21bfe34b54f3"),
  id: 1,
  secure_code: '01H4EEMGMG9VADVF06JZGJJGN0',
  airline: 'EasyFly',
  departure_city: 'Berlin',
  departure_date: '25/12/2022',
  arrival_airport: 'PEI',
  arrival_city: 'Pereira',
  arrival_time: '27/12/2022 14:13',
  passenger_name: 'Nathalie Cardona',
  passenger_gender: 'Female',
  seat_number: 'A1',
  currency: 'EUR',
  departure_gate: 'B2',
  flight_status: 'On Time',
  co_pilot_name: 'Hart Blunkett',
  aircraft_type: 'Embraer E190',
  fuel_consumption: 7916.39,
  VueloId: [
    {
      _id: ObjectId("64bb5eb2a21e5a2e74b36a20"),
      flight_id: 1,
      flight_number: 1978,
      departure_airport: 'CFQ',
      departure_country: 'Germany',
      departure_time: '6/7/2023 04:42',
      arrival_country: 'Colombia',
      arrival_date: '27/12/2022',
      flight_duration: 14.18,
      passenger_age: 0,
      passenger_nationality: 'Colombia',
      ticket_price: 797.24,
      baggage_weight: 43.85,
      arrival_gate: 'E5',
      pilot_name: 'Sunny Few',
      cabin_crew_count: 9,
      aircraft_registration: 'N12345',
      flight_distance: 1400.24
    }
  ]
}
```


# OBTENER SOLO EL PRIMER DOCUMENTO DE UNA COLECCION
`db.vuelos_1.findOne()`
```mongodb
{
  _id: ObjectId("64ba0cea510b21bfe34b54f3"),
  id: 1,
  secure_code: '01H4EEMGMG9VADVF06JZGJJGN0',
  airline: 'EasyFly',
  departure_city: 'Berlin',
  departure_date: '25/12/2022',
  arrival_airport: 'PEI',
  arrival_city: 'Pereira',
  arrival_time: '27/12/2022 14:13',
  passenger_name: 'Nathalie Cardona',
  passenger_gender: 'Female',
  seat_number: 'A1',
  currency: 'EUR',
  departure_gate: 'B2',
  flight_status: 'On Time',
  co_pilot_name: 'Hart Blunkett',
  aircraft_type: 'Embraer E190',
  fuel_consumption: 7916.39
}
```

# VER EL ULTIMO ELEMENTO DE UNA COLECCION
```mongodb
collection.find_one({}, sort=[('_id', -1)])
```

```mongodb

```

------------------------
# SI QUIERE TENER LOS VALORES SIN ANIDAR UNA DE LAS COLECCIONES
# PRIMERO LOS CAMPOS DE LA PRIMERA COLECCION

```mongodb
db.vuelos_1.aggregate([
  {
    $lookup: {
      from: "vuelos_2",
      localField: "id",
      foreignField: "flight_id",
      as: "VueloId"
    }
  },
  {
    $unwind: {
      path: "$VueloId",
      preserveNullAndEmptyArrays: true
    }
  },
  {
    $replaceRoot: {
      newRoot: {
        $mergeObjects: ["$$ROOT","$VueloId"]
      }
    }
  },
  {
    $project: {
      VueloId: 0,
	   _id: 0
    }
  },
  {
    $limit: 1
  }
]);
```
# RESPUESTA
```mongodb
{
  id: 1,
  secure_code: '01H4EEMGMG9VADVF06JZGJJGN0',
  airline: 'EasyFly',
  departure_city: 'Berlin',
  departure_date: '25/12/2022',
  arrival_airport: 'PEI',
  arrival_city: 'Pereira',
  arrival_time: '27/12/2022 14:13',
  passenger_name: 'Nathalie Cardona',
  passenger_gender: 'Female',
  seat_number: 'A1',
  currency: 'EUR',
  departure_gate: 'B2',
  flight_status: 'On Time',
  co_pilot_name: 'Hart Blunkett',
  aircraft_type: 'Embraer E190',
  fuel_consumption: 7916.39,
  flight_id: 1,
  flight_number: 1978,
  departure_airport: 'CFQ',
  departure_country: 'Germany',
  departure_time: '6/7/2023 04:42',
  arrival_country: 'Colombia',
  arrival_date: '27/12/2022',
  flight_duration: 14.18,
  passenger_age: 0,
  passenger_nationality: 'Colombia',
  ticket_price: 797.24,
  baggage_weight: 43.85,
  arrival_gate: 'E5',
  pilot_name: 'Sunny Few',
  cabin_crew_count: 9,
  aircraft_registration: 'N12345',
  flight_distance: 1400.24
}
```

# PRIMERO LOS CAMPOS DE LA SEGUNDA COLECCION

```mongodb
db.vuelos_1.aggregate([
  {
    $lookup: {
      from: "vuelos_2",
      localField: "id",
      foreignField: "flight_id",
      as: "VueloId"
    }
  },
  {
    $unwind: {
      path: "$VueloId",
      preserveNullAndEmptyArrays: true
    }
  },
  {
    $replaceRoot: {
      newRoot: {
        $mergeObjects: ["$VueloId", "$$ROOT"]
      }
    }
  },
  {
    $project: {
      VueloId: 0,
	   _id: 0
    }
  },
  {
    $limit: 1
  }
]);
```
# RESPUESTA
```mongodb
{
  flight_id: 1,
  flight_number: 1978,
  departure_airport: 'CFQ',
  departure_country: 'Germany',
  departure_time: '6/7/2023 04:42',
  arrival_country: 'Colombia',
  arrival_date: '27/12/2022',
  flight_duration: 14.18,
  passenger_age: 0,
  passenger_nationality: 'Colombia',
  ticket_price: 797.24,
  baggage_weight: 43.85,
  arrival_gate: 'E5',
  pilot_name: 'Sunny Few',
  cabin_crew_count: 9,
  aircraft_registration: 'N12345',
  flight_distance: 1400.24,
  id: 1,
  secure_code: '01H4EEMGMG9VADVF06JZGJJGN0',
  airline: 'EasyFly',
  departure_city: 'Berlin',
  departure_date: '25/12/2022',
  arrival_airport: 'PEI',
  arrival_city: 'Pereira',
  arrival_time: '27/12/2022 14:13',
  passenger_name: 'Nathalie Cardona',
  passenger_gender: 'Female',
  seat_number: 'A1',
  currency: 'EUR',
  departure_gate: 'B2',
  flight_status: 'On Time',
  co_pilot_name: 'Hart Blunkett',
  aircraft_type: 'Embraer E190',
  fuel_consumption: 7916.39
}
```
# ADICIONA LOS _id DE CADA COLECCION CON ALIAS
```mongodb
db.vuelos_1.aggregate([
  {
    $lookup: {
      from: "vuelos_2",
      localField: "id",
      foreignField: "flight_id",
      as: "coleccion_vuelos_2"
    }
  },
  {
    $unwind: {
      path: "$coleccion_vuelos_2",
      preserveNullAndEmptyArrays: true
    }
  },
  {
    $addFields: {
      _id_coleccion_vuelos_1: "$_id",
      _id_coleccion_vuelos_2: "$coleccion_vuelos_2._id"
    }
  },
  {
    $replaceRoot: {
      newRoot: {
        $mergeObjects: [
          { _id_coleccion_vuelos_1: "$_id_coleccion_vuelos_1"},
		  "$$ROOT",
		  {_id_coleccion_vuelos_2: "$_id_coleccion_vuelos_2" },
		  "$coleccion_vuelos_2"
        ]
      }
    }
  },
  {
    $project: {
      coleccion_vuelos_2: 0,
      _id: 0
    }
  },
  {
    $limit: 1
  }
]);
```
# RESPUESTA
```mongodb
{
  _id_vuelos_1: ObjectId("64ba0cea510b21bfe34b54f3"),
  id: 1,
  secure_code: '01H4EEMGMG9VADVF06JZGJJGN0',
  airline: 'EasyFly',
  departure_city: 'Berlin',
  departure_date: '25/12/2022',
  arrival_airport: 'PEI',
  arrival_city: 'Pereira',
  arrival_time: '27/12/2022 14:13',
  passenger_name: 'Nathalie Cardona',
  passenger_gender: 'Female',
  seat_number: 'A1',
  currency: 'EUR',
  departure_gate: 'B2',
  flight_status: 'On Time',
  co_pilot_name: 'Hart Blunkett',
  aircraft_type: 'Embraer E190',
  fuel_consumption: 7916.39,
  _id_vuelos_2: ObjectId("64bb5eb2a21e5a2e74b36a20"),
  flight_id: 1,
  flight_number: 1978,
  departure_airport: 'CFQ',
  departure_country: 'Germany',
  departure_time: '6/7/2023 04:42',
  arrival_country: 'Colombia',
  arrival_date: '27/12/2022',
  flight_duration: 14.18,
  passenger_age: 0,
  passenger_nationality: 'Colombia',
  ticket_price: 797.24,
  baggage_weight: 43.85,
  arrival_gate: 'E5',
  pilot_name: 'Sunny Few',
  cabin_crew_count: 9,
  aircraft_registration: 'N12345',
  flight_distance: 1400.24
}
```