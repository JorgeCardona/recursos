# CREAR UN JOIN UNA VISTA EN MONGODB
https://www.mongodb.com/docs/relational-migrator/code-generation/query-converter/convert-views/#std-label-rm-convert-views

### Regular Queries
<img src="imagenes\07_mongodb_regular_queries.png">

### Inner Join
<img src="imagenes\08_mongodb_inner_join.png">

### View 1
<img src="imagenes\09_mongodb_view_1.png">

### View 2
<img src="imagenes\10_mongodb_view_2.png">


# PAQUETE COLLECIONES
```
 # EL MODULO deque EN PYTHON SE PUEDE COMPORTAR COMO COLA O COMO PILA, DEPENDIENDO DE LOS METODOS DE INSERCION O RECUPERACION DE ELEMENTOS A USAR
from collections import deque
lista_valores = [0,1,2,7,3,7,7,4,5,6,7,8,9,7]
lista_2 = [13,31,1978,12,27]


queue = deque(lista_valores)
queue.reverse()
print(f'{list(queue)}, deque orden inverso') # [7, 9, 8, 7, 6, 5, 4, 7, 7, 3, 7, 2, 1, 0]

queue = deque(lista_valores)
print(f'{list(queue)}, deque orden normal') # [0,1,2,7,3,7,7,4,5,6,7,8,9,7]

queue = deque(lista_valores)
queue.rotate(3)
print(f'{list(queue)}, deque orden rotado 3 posiciones') # [8, 9, 7, 0, 1, 2, 7, 3, 7, 7, 4, 5, 6, 7]
print()

queue = deque(lista_valores)
print(f'{list(queue)}, deque orden actual') # [0,1,2,7,3,7,7,4,5,6,7,8,9,7]
queue = deque(lista_valores)
print(f'{queue.pop()}, deque recupera el ultimo elemento de la derecha') # 7
print(f'{queue.popleft()}, deque recupera el primer elemento de la izquierda') # 0
print()

print(f'{queue.append(5)}, deque adiciona el ultimo elemento de la derecha 5') # 5
print(f'{queue.appendleft(9)}, deque adiciona el primer elemento de la izquierda 9') # 9
print()

print(f'{queue.count(7)} veces, deque recupera la cantidad de veces que aparece el elemento 7')
print(f'{queue.insert(5, 99)}, inserta el 99 en el indice 5')
print(f'{queue.extend(lista_2)}, deque adiciona una lista {lista_2} el ultimo elemento de la derecha')
print(f'{queue.extendleft(lista_2)}, deque adiciona una lista {lista_2} como el primer elemento de la izquierda, de manera invertida')
print(f'indice {queue.index(31)}, deque obtiene el indice de la primera aparicion del numero 31') # indice 3
print(f'indice {queue.remove(1978)}, deque elimina la primera aparicion del numero 1978')
print(f'{list(queue)}, deque recupera los elementos restantes de la deque') # [27, 12, 31, 13, 9, 1, 2, 7, 3, 99, 7, 7, 4, 5, 6, 7, 8, 9, 5, 13, 31, 1978, 12, 27]


# Crear un deque con un tamaño máximo de 5 elementos
maxlen_deque = deque(maxlen=3)
maxlen_deque.extend(lista_2)
print(f'{list(maxlen_deque)}, deque recupera los elementos de la list {lista_2} definidos como el maximo tamano de la deque en este caso') # [1978, 12, 27] de [13, 31, 1978, 12, 27]
```


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

# CURSOR
Es una estructura iterable, similar a una lista de diccionarios en python. donde se almacenan los resultados de las consultas. se genera al hacer uso del metodo **.find()**

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

# VER EL ULTIMO DOCUMENTO DE UNA COLECCION ORDENANDOLO POR LA LLAVE PRIMARIA
```mongodb
db.vuelos_1.find()
           .sort(
                  {
                    _id: -1
                  }
                 )
                 .limit(1)
```

```mongodb
{
  _id: ObjectId("64ba0ceb510b21bfe34b687a"),
  id: 5000,
  secure_code: '01H4EEN2EGF42MW38WSMVFQKJF',
  airline: 'United',
  departure_city: 'Pueblo',
  departure_date: '11/7/2022',
  arrival_airport: 'GBM',
  arrival_city: 'Örbyhus',
  arrival_time: '6/7/2023 06:15',
  passenger_name: 'Huntington MacNeil',
  passenger_gender: 'Male',
  seat_number: 'C3',
  currency: 'USD',
  departure_gate: 'B2',
  flight_status: 'Delayed',
  co_pilot_name: 'Mandel Navarre',
  aircraft_type: 'Boeing 737',
  fuel_consumption: 1632.85
}
```

# INCLUIR SOLO LOS CAMPOS QUE SE QUIEREN DEL DOCUMENTO 1 PARA INCLUIR EL CAMPO, 0 PARA EVITAR ESE CAMPO
```mongodb
db.vuelos_1.find(
  {},
  {
    _id: 0,
    arrival_city:1,
    passenger_name: 1
  }
)
```
```mongodb
{
  arrival_city: 'Pereira',
  passenger_name: 'Nathalie Cardona'
}
...
...
...
{
  arrival_city: 'Örbyhus',
  passenger_name: 'Huntington MacNeil'
}
```

# EXCLUIR TODOS LOS CAMPOS QUE NO SE NECESITAN
```mongodb
db.vuelos_1.find(
  {},
  {
    _id: 0,
    secure_code:0,
    departure_gate:0,
    flight_status:0,
    co_pilot_name:0,
    aircraft_type:0,
    fuel_consumption:0,
    passenger_gender:0,
    departure_date:0,
    seat_number:0
  }
)
```
```mongodb
{
  id: 1,
  airline: 'EasyFly',
  departure_city: 'Berlin',
  arrival_airport: 'PEI',
  arrival_city: 'Pereira',
  arrival_time: '27/12/2022 14:13',
  passenger_name: 'Nathalie Cardona',
  currency: 'EUR'
}
...
...
...
{
  id: 5000,
  airline: 'United',
  departure_city: 'Pueblo',
  arrival_airport: 'GBM',
  arrival_city: 'Örbyhus',
  arrival_time: '6/7/2023 06:15',
  passenger_name: 'Huntington MacNeil',
  currency: 'USD'
}
```


# VER LIMITE DE n DOCUMENTOS DE UNA COLECCION
```mongodb
var n = 3
db.vuelos_1.find()
           .limit(n)
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
{
  _id: ObjectId("64ba0cea510b21bfe34b54f5"),
  id: 3,
  secure_code: '01H4EEMGN3BZJ9RR779KDEB2WG',
  airline: 'United',
  departure_city: 'Oyo',
  departure_date: '3/4/2022',
  arrival_airport: 'KWJ',
  arrival_city: 'Jabon',
  arrival_time: '6/7/2023 03:44',
  passenger_name: 'Fifine Luten',
  passenger_gender: 'Female',
  seat_number: 'B2',
  currency: 'NGN',
  departure_gate: 'C3',
  flight_status: 'On Time',
  co_pilot_name: 'Christie Wakeley',
  aircraft_type: 'Boeing 737',
  fuel_consumption: 8047.44
}
```

# VER LIMITE DE LOS ULTIMOS n DOCUMENTOS DE UNA COLECCION, ORDENADO DESDE EL MENOR AL ULTIMO
```mongodb
var n = 3
db.vuelos_1.find()
           .sort(
                  {
                    _id: -1
                  }
                )
            .limit(n)
            .toArray()
            .reverse()
```

```mongodb
[
  {
    _id: ObjectId("64ba0ceb510b21bfe34b6878"),
    id: 4998,
    secure_code: '01H4EEN2E852X2Q243QKGY8K6X',
    airline: 'United',
    departure_city: 'Kazo',
    departure_date: '12/10/2022',
    arrival_airport: 'FKL',
    arrival_city: 'Glazov',
    arrival_time: '6/7/2023 08:34',
    passenger_name: 'Elisabet Halbeard',
    passenger_gender: 'Female',
    seat_number: 'A1',
    currency: 'JPY',
    departure_gate: 'B2',
    flight_status: 'Delayed',
    co_pilot_name: 'Ardisj Lembke',
    aircraft_type: 'Airbus A320',
    fuel_consumption: 9120.71
  },
  {
    _id: ObjectId("64ba0ceb510b21bfe34b6879"),
    id: 4999,
    secure_code: '01H4EEN2ECWBYQ6CZ3GP31Q61B',
    airline: 'Delta',
    departure_city: 'Dallas',
    departure_date: '15/11/2022',
    arrival_airport: 'KVB',
    arrival_city: 'Boychinovtsi',
    arrival_time: '6/7/2023 05:31',
    passenger_name: 'Allard Milligan',
    passenger_gender: 'Male',
    seat_number: 'C3',
    currency: 'USD',
    departure_gate: 'C3',
    flight_status: 'On Time',
    co_pilot_name: 'Jarid Jonson',
    aircraft_type: 'Airbus A320',
    fuel_consumption: 8674.24
  },
  {
    _id: ObjectId("64ba0ceb510b21bfe34b687a"),
    id: 5000,
    secure_code: '01H4EEN2EGF42MW38WSMVFQKJF',
    airline: 'United',
    departure_city: 'Pueblo',
    departure_date: '11/7/2022',
    arrival_airport: 'GBM',
    arrival_city: 'Örbyhus',
    arrival_time: '6/7/2023 06:15',
    passenger_name: 'Huntington MacNeil',
    passenger_gender: 'Male',
    seat_number: 'C3',
    currency: 'USD',
    departure_gate: 'B2',
    flight_status: 'Delayed',
    co_pilot_name: 'Mandel Navarre',
    aircraft_type: 'Boeing 737',
    fuel_consumption: 1632.85
  }
]
```

# VER LIMITE DE LOS PRIMEROS n DOCUMENTOS DE UNA COLECCION, DESPUES DE x DOCUMENTOS OFFSET
```mongodb
var n = 3
var x = 10
db.vuelos_1.find()
            .skip(x)
            .limit(n)
```

```mongodb
{
  _id: ObjectId("64ba0cea510b21bfe34b54fd"),
  id: 11,
  secure_code: '01H4EEMGPGM90HM7BKHTEME44X',
  airline: 'Delta',
  departure_city: 'Forninho',
  departure_date: '15/1/2022',
  arrival_airport: 'PRM',
  arrival_city: 'Kornyn',
  arrival_time: '6/7/2023 08:00',
  passenger_name: 'Hoebart Fruchon',
  passenger_gender: 'Male',
  seat_number: 'C3',
  currency: 'EUR',
  departure_gate: 'B2',
  flight_status: 'Delayed',
  co_pilot_name: 'Cesare Janovsky',
  aircraft_type: 'Embraer E190',
  fuel_consumption: 6868.05
}
{
  _id: ObjectId("64ba0cea510b21bfe34b54fe"),
  id: 12,
  secure_code: '01H4EEMGPP9H8CR43QP3J6PW42',
  airline: 'American',
  departure_city: 'Lomboy',
  departure_date: '16/3/2022',
  arrival_airport: 'DMU',
  arrival_city: 'Ballinteer',
  arrival_time: '6/7/2023 00:25',
  passenger_name: 'Rockie Huett',
  passenger_gender: 'Male',
  seat_number: 'C3',
  currency: 'PHP',
  departure_gate: 'B2',
  flight_status: 'Cancelled',
  co_pilot_name: 'Zerk Le Hucquet',
  aircraft_type: 'Boeing 737',
  fuel_consumption: 5346.91
}
{
  _id: ObjectId("64ba0cea510b21bfe34b54ff"),
  id: 13,
  secure_code: '01H4EEMGPVCXFW2VZ66JBD7Q4M',
  airline: 'United',
  departure_city: 'Essang',
  departure_date: '23/10/2022',
  arrival_airport: 'WLA',
  arrival_city: 'Três Passos',
  arrival_time: '6/7/2023 16:28',
  passenger_name: 'Lorrin Armit',
  passenger_gender: 'Female',
  seat_number: 'A1',
  currency: 'IDR',
  departure_gate: 'B2',
  flight_status: 'Cancelled',
  co_pilot_name: 'Inessa Bradnock',
  aircraft_type: 'Embraer E190',
  fuel_consumption: 7185.9
}
```

# VER LIMITE DE LOS ULTIMOS n DOCUMENTOS DE UNA COLECCION, COMENZANDO DESDE x DOCUMENTOS OFFSET
```mongodb
db.vuelos_1.find().sort(
  {
    _id: -1
  }
)
.skip(x)
.limit(n)
.toArray()
.reverse()
```

```mongodb
[
  {
    _id: ObjectId("64ba0ceb510b21bfe34b686e"),
    id: 4988,
    secure_code: '01H4EEN2CYJJKKSFZ3MD328Z7M',
    airline: 'American',
    departure_city: 'Cotorra',
    departure_date: '15/11/2022',
    arrival_airport: 'ZRJ',
    arrival_city: 'Azurva',
    arrival_time: '6/7/2023 06:55',
    passenger_name: 'Nicolea Darnell',
    passenger_gender: 'Female',
    seat_number: 'B2',
    currency: 'COP',
    departure_gate: 'B2',
    flight_status: 'Cancelled',
    co_pilot_name: 'Tedda Surgison',
    aircraft_type: 'Airbus A320',
    fuel_consumption: 6868.56
  },
  {
    _id: ObjectId("64ba0ceb510b21bfe34b686f"),
    id: 4989,
    secure_code: '01H4EEN2D2JNYTDHCS7XYESGH8',
    airline: 'United',
    departure_city: 'Karuk',
    departure_date: '13/9/2022',
    arrival_airport: 'GRH',
    arrival_city: 'Chumpi',
    arrival_time: '6/7/2023 18:54',
    passenger_name: 'Kellyann Joinsey',
    passenger_gender: 'Female',
    seat_number: 'C3',
    currency: 'IDR',
    departure_gate: 'B2',
    flight_status: 'Cancelled',
    co_pilot_name: 'Delly Horsted',
    aircraft_type: 'Boeing 737',
    fuel_consumption: 2467.74
  },
  {
    _id: ObjectId("64ba0ceb510b21bfe34b6870"),
    id: 4990,
    secure_code: '01H4EEN2D7Q1D03WJ07Y9DQ0Y9',
    airline: 'United',
    departure_city: 'Małdyty',
    departure_date: '9/9/2022',
    arrival_airport: 'TMG',
    arrival_city: 'Besuki',
    arrival_time: '6/7/2023 05:58',
    passenger_name: 'Modestine Labusch',
    passenger_gender: 'Female',
    seat_number: 'A1',
    currency: 'PLN',
    departure_gate: 'A1',
    flight_status: 'Cancelled',
    co_pilot_name: 'Essy Jebb',
    aircraft_type: 'Embraer E190',
    fuel_consumption: 7818.02
  }
]
```

# VER DOCUMENTOS DE UNA COLECCION, QUE COINCIDAN CON UNA CONSULTA DE UNA LLAVE
```mongodb
db.vuelos_1.find(
  {
    seat_number: 'A1'
  }
)
.limit(2)
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
  _id: ObjectId("64ba0cea510b21bfe34b54f7"),
  id: 5,
  secure_code: '01H4EEMGNFX6T41V6RSST9YVPF',
  airline: 'Delta',
  departure_city: 'Ko Pha Ngan',
  departure_date: '10/7/2022',
  arrival_airport: 'QUB',
  arrival_city: 'Sovetskaya Gavan’',
  arrival_time: '6/7/2023 16:55',
  passenger_name: 'Norman Crosen',
  passenger_gender: 'Male',
  seat_number: 'A1',
  currency: 'THB',
  departure_gate: 'A1',
  flight_status: 'On Time',
  co_pilot_name: 'Barn Timmes',
  aircraft_type: 'Boeing 737',
  fuel_consumption: 7584.07
}
```

# CONTAR TODOS LOS DOCUMENTOS DE UNA COLECCION
```mongodb
db.vuelos_1.find().count()
5000
```

# CONTAR CUANTOS DOCUMENTOS COINCIDEN CON LA CONSULTA
```mongodb
db.vuelos_1.find(
  {
    seat_number: 'A1'
  }
)
.count()
```

```mongodb
1683
```

# LISTAR LOS VALORES UNICOS QUE HAY EN UN CAMPO EN UNA COLECCION
```mongodb
db.vuelos_1.distinct('seat_number')
```

```mongodb
[ 'A1', 'B2', 'C3' ]
```

# CONTAR CUANTOS VALORES UNICOS TIENE UNA LLAVE EN UNA COLECCION
```mongodb
db.vuelos_1.distinct('seat_number').length
3
```

# MOSTRAR TODOS LOS DOCUMENTOS DE UNA COLECCION DONDE LA LLAVE TENGA UN VALOR IGUAL AL SOLICITADO
```mongodb
db.vuelos_1.find(
  {
    fuel_consumption:{ $eq:7916.39 }
  }
)
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
```

# MOSTRAR TODOS LOS DOCUMENTOS DE UNA COLECCION DONDE LA LLAVE TENGA UN VALOR DIFERENTE (NO IGUAL) AL CONSULTADO
```mongodb
db.vuelos_1.find(
  {
    fuel_consumption:{ $ne:7916.39 }
  }
)
.count()
4999
```

# MOSTRAR TODOS LOS DOCUMENTOS DE UNA COLECCION DONDE LA LLAVE TENGA UN VALOR MENOR (<), MENOR O IGUAL(<=) AL CONSULTADO
```mongodb
db.vuelos_1.find(
  {
    fuel_consumption:{ $lt:7916.39 }
  }
)
.count()
```

```mongodb
db.vuelos_1.find(
  {
    fuel_consumption:{ $lte:7916.39 }
  }
)
.count()
```

# MOSTRAR TODOS LOS DOCUMENTOS DE UNA COLECCION DONDE LA LLAVE TENGA UN VALOR MAYOR (>), MAYOR O IGUAL(>=) AL CONSULTADO
```mongodb
db.vuelos_1.find(
  {
    fuel_consumption:{ $gt:7916.39 }
  }
)
.count()
```

```mongodb
db.vuelos_1.find(
  {
    fuel_consumption:{ $gte:7916.39 }
  }
)
.count()
```

# USAR EL OPERADOR OR
```mongodb
db.vuelos_1.find({
  $or: [
        { 
          fuel_consumption: { $eq: 7916.39 } 
        },
        { 
          passenger_gender: { $eq:'Female' } 
        }
      ]
})
.count()
```

```mongodb
2257
```

# USAR EL OPERADOR AND, CALCULANDO UN RANGO DE VALORES
```mongodb
db.vuelos_1.find({
  $and: [
          {
            fuel_consumption: { $gte:7915 } 
          },
          {
            fuel_consumption: { $lte:7917}
          }
        ]
})
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
  _id: ObjectId("64ba0cea510b21bfe34b5ee7"),
  id: 2549,
  secure_code: '01H4EEMT9WC5W3CZP84SBRXX6T',
  airline: 'American',
  departure_city: 'Inglewood',
  departure_date: '3/2/2022',
  arrival_airport: 'TEO',
  arrival_city: 'Kebon',
  arrival_time: '6/7/2023 12:40',
  passenger_name: 'Rudie Dunkerley',
  passenger_gender: 'Non-binary',
  seat_number: 'B2',
  currency: 'USD',
  departure_gate: 'A1',
  flight_status: 'On Time',
  co_pilot_name: 'Jozef Phillpotts',
  aircraft_type: 'Embraer E190',
  fuel_consumption: 7916.91
}
```

# CONSULTAR DOCUMENTOS QUE EN UN CAMPO INCLUYAN UN VALOR ESPECIFICO
```mongodb
db.vuelos_1.find({
  seat_number: { $in: ['A1','B1','C1']}
})
.count()
```

```
1683
```

# CONSULTAR DOCUMENTOS QUE EN UN CAMPO NO INCLUYAN UN VALOR ESPECIFICO
```mongodb
db.vuelos_1.find({
  seat_number: { $nin: ['A1','B1','C1']}
})
.count()
```

```
3317
```

# CONSULTAR DOCUMENTOS QUE EN UN CAMPO NO INCLUYAN UN VALOR ESPECIFICO
```mongodb
db.vuelos_1.find({
  $nor: [
    { 
		fuel_consumption: { $gte: 7915, $lte: 7917 } 
	},
    { 
		seat_number: { $nin: ['A1','B1','C1']}
	}
  ]
})
.count()
```

# VALIDAR EN QUE DOCUMENTOS EXISTE UN CAMPO ESPECIFICO
```mongodb
db.vuelos_1.find({
  arrival_city: { $exists: true}
})
.count()
```

```mongodb
5000
```

# VALIDAR EN QUE DOCUMENTOS EXISTE UN TIPO DE DATO ESPECIFICO

```mongodb
db.vuelos_1.find({
  id: { $type: 'number'}
})
.count()
```

```mongodb
5000
```

# BUSCAR BASADO EN TEXTO
### CREAR UN INDICE EN LA COLUMNA A BUSCAR
```mongodb
// Crear un índice de texto en el campo "arrival_city", con palabra exacta
db.vuelos_1.createIndex(
  { arrival_city: "text" },
  { name: "index_arrival_city" }
);

# Indice con busqueda en el camppo passenger_name con expresion Regular
db.vuelos_1.createIndex(
  { passenger_name: 1 },
  {
    name: "index_passenger_name",
    collation: { locale: "en", strength: 2 },
    partialFilterExpression: { passenger_name: { $type: "string" } }
  }
);
```

# LISTAR LOS INDICES

```mongodb
db.vuelos_1.getIndexes()
```

```mongodb
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  {
    v: 2,
    key: { passenger_name: 1 },
    name: 'index_passenger_name',
    partialFilterExpression: { passenger_name: [Object] },
    collation: {
      locale: 'en',
      caseLevel: false,
      caseFirst: 'off',
      strength: 2,
      numericOrdering: false,
      alternate: 'non-ignorable',
      maxVariable: 'punct',
      normalization: false,
      backwards: false,
      version: '57.1'
    }
  },
  {
    v: 2,
    key: { _fts: 'text', _ftsx: 1 },
    name: 'index_arrival_city',
    weights: { arrival_city: 1 },
    default_language: 'english',
    language_override: 'language',
    textIndexVersion: 3
  }
]
```

# BUSCAR USANDO EL INDICE
```mongodb
// Realizar una consulta de búsqueda de texto
db.vuelos_1.find(
                  {
                    $text: { $search: "pereira" }
                  }
                )
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
  _id: ObjectId("64ba0cea510b21bfe34b5729"),
  id: 567,
  secure_code: '01H4EEMKDEJC60KWB8C9VB3126',
  airline: 'American',
  departure_city: 'Bajos de Haina',
  departure_date: '13/9/2022',
  arrival_airport: 'SAR',
  arrival_city: 'Pereira',
  arrival_time: '6/7/2023 19:41',
  passenger_name: 'Dunc Dumsday',
  passenger_gender: 'Genderfluid',
  seat_number: 'B2',
  currency: 'DOP',
  departure_gate: 'C3',
  flight_status: 'On Time',
  co_pilot_name: 'Dexter Poskitt',
  aircraft_type: 'Airbus A320',
  fuel_consumption: 1066.7
}
```

# USO DEL INDICE CON EXPRESION REGULAR
```mongodb
db.vuelos_1.find(
                  { 
                    passenger_name: /^Nathalie/ 
                  }
                );
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
```

# BUSQUEDA NO SENSIBLE AL CASO
```mongodb
db.vuelos_1.find(
                  { 
                    passenger_name: { 
                                      $regex: 'thalie', 
                                      $options: 'i' 
                                    } 
                  }
                );
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
```

# ELIMINAR UN INDICE

```mongodb
db.vuelos_1.dropIndexes(['index_passenger_name', 'index_arrival_city'])
```

```mongodb
{ nIndexesWas: 2, ok: 1 }
```

# INSERTAR DOCUMENTOS

# EL METODO INSERT
```mongodb
db.vuelos_1.insert({
  id: 9998,
  secure_code: 'XYZ456',
  airline: 'FlyAway Airlines',
  departure_city: 'London',
  departure_date: '2023-08-15',
  arrival_airport: 'CDG',
  arrival_city: 'Paris',
  arrival_time: '2023-08-15 18:45',
  passenger_name: 'Emily Brown',
  passenger_gender: 'Female',
  seat_number: 'A3',
  currency: 'EUR',
  departure_gate: 'C2',
  flight_status: 'Delayed',
  co_pilot_name: 'David Wilson',
  aircraft_type: 'Airbus A320',
  fuel_consumption: 7200.00
});
```

# INSERT ONE
```mongodb
db.vuelos_1.insertOne({
  id: 9999,
  secure_code: 'ABC123',
  airline: 'AirTravel Inc.',
  departure_city: 'New York',
  departure_date: '2023-07-25',
  arrival_airport: 'LAX',
  arrival_city: 'Los Angeles',
  arrival_time: '2023-07-25 14:30',
  passenger_name: 'John Smith',
  passenger_gender: 'Male',
  seat_number: 'C5',
  currency: 'USD',
  departure_gate: 'B4',
  flight_status: 'On Time',
  co_pilot_name: 'Jane Johnson',
  aircraft_type: 'Boeing 737',
  fuel_consumption: 8500.00
});
```

# INSERTAR MULTIPLES DOCUMENTO

```mongodb
var lista_documentos = [
  {
    id: 10001,
    secure_code: 'DEF456',
    airline: 'AirConnect',
    departure_city: 'Tokyo',
    departure_date: '2023-08-25',
    arrival_airport: 'ICN',
    arrival_city: 'Seoul',
    arrival_time: '2023-08-25 10:15',
    passenger_name: 'Aiko Tanaka',
    passenger_gender: 'Female',
    seat_number: 'C1',
    currency: 'JPY',
    departure_gate: 'D3',
    flight_status: 'On Time',
    co_pilot_name: 'Takashi Suzuki',
    aircraft_type: 'Boeing 777',
    fuel_consumption: 9500.00
  },
  {
    id: 10002,
    secure_code: 'GHI789',
    airline: 'FlyNow',
    departure_city: 'London',
    departure_date: '2023-09-10',
    arrival_airport: 'CDG',
    arrival_city: 'Paris',
    arrival_time: '2023-09-10 18:45',
    passenger_name: 'Sophie Dupont',
    passenger_gender: 'Female',
    seat_number: 'D5',
    currency: 'EUR',
    departure_gate: 'B4',
    flight_status: 'Delayed',
    co_pilot_name: 'Jean-Pierre Martin',
    aircraft_type: 'Airbus A320',
    fuel_consumption: 7000.00
  },
  {
    id: 10003,
    secure_code: 'JKL012',
    airline: 'OceanAir',
    departure_city: 'Sydney',
    departure_date: '2023-09-15',
    arrival_airport: 'AKL',
    arrival_city: 'Auckland',
    arrival_time: '2023-09-15 08:00',
    passenger_name: 'Liam Johnson',
    passenger_gender: 'Male',
    seat_number: 'E3',
    currency: 'AUD',
    departure_gate: 'G2',
    flight_status: 'On Time',
    co_pilot_name: 'Emma Wilson',
    aircraft_type: 'Airbus A380',
    fuel_consumption: 11000.00
  },
  {
    id: 10004,
    secure_code: 'MNO345',
    airline: 'SunAir',
    departure_city: 'Rio de Janeiro',
    departure_date: '2023-09-20',
    arrival_airport: 'BUE',
    arrival_city: 'Buenos Aires',
    arrival_time: '2023-09-20 12:30',
    passenger_name: 'Sofia Martinez',
    passenger_gender: 'Female',
    seat_number: 'F2',
    currency: 'BRL',
    departure_gate: 'E1',
    flight_status: 'On Time',
    co_pilot_name: 'Carlos Ramirez',
    aircraft_type: 'Embraer E195',
    fuel_consumption: 6800.00
  },
  {
  id: 10005,
  secure_code: 'PQR678',
  airline: 'ColombiaAir',
  departure_city: 'Bogotá',
  departure_date: '2023-09-25',
  arrival_airport: 'MDE',
  arrival_city: 'Medellín',
  arrival_time: '2023-09-25 14:00',
  passenger_name: 'Andrés Gómez',
  passenger_gender: 'Male',
  seat_number: 'A3',
  currency: 'COP',
  departure_gate: 'B1',
  flight_status: 'On Time',
  co_pilot_name: 'Laura Rodríguez',
  aircraft_type: 'Airbus A319',
  fuel_consumption: 6000.00
 },
]

db.vuelos_1.insertMany(lista_documentos);
```

```mongodb
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId("64d16c4d63e205aadb7039a9"),
    '1': ObjectId("64d16c4d63e205aadb7039aa"),
    '2': ObjectId("64d16c4d63e205aadb7039ab"),
    '3': ObjectId("64d16c4d63e205aadb7039ac"),
    '4': ObjectId("64d16c4d63e205aadb7039ad")
  }
}
```

# BULKWRITE
Este método se utiliza para realizar operaciones en masa, como inserciones, actualizaciones y eliminaciones en una sola llamada.

Recibe como argumento un arreglo de operaciones, donde cada operación es un objeto que especifica qué acción realizar en un documento.

Puede realizar operaciones en diferentes colecciones y tipos de operaciones en la misma llamada.
Retorna un objeto con información sobre las operaciones ejecutadas.

```mongodb
db.vuelos_1.bulkWrite([
  {
    insertOne: {
      document: {
        id: 10006,
        secure_code: 'ABC123',
        airline: 'ExampleAir',
        departure_city: 'New York',
        departure_date: '2023-07-20',
        arrival_airport: 'JFK',
        arrival_city: 'Los Angeles',
        arrival_time: '2023-07-20 12:00',
        passenger_name: 'John Doe',
        passenger_gender: 'Male',
        seat_number: 'B2',
        currency: 'USD',
        departure_gate: 'A2',
        flight_status: 'Delayed',
        co_pilot_name: 'Jane Smith',
        aircraft_type: 'Boeing 737',
        fuel_consumption: 7500.00
      }
    }
  },
  {
    insertOne: {
      document: {
        id: 10007,
        secure_code: 'XYZ789',
        airline: 'TravelAir',
        departure_city: 'London',
        departure_date: '2023-07-21',
        arrival_airport: 'LHR',
        arrival_city: 'Paris',
        arrival_time: '2023-07-21 15:30',
        passenger_name: 'Maria Gonzalez',
        passenger_gender: 'Female',
        seat_number: 'C1',
        currency: 'EUR',
        departure_gate: 'C3',
        flight_status: 'On Time',
        co_pilot_name: 'Carlos Ramirez',
        aircraft_type: 'Airbus A320',
        fuel_consumption: 6800.00
      }
    }
  },
  {
    insertOne: {
      document: {
        id: 10008,
        secure_code: 'LMN456',
        airline: 'FlyNow',
        departure_city: 'Tokyo',
        departure_date: '2023-07-22',
        arrival_airport: 'HND',
        arrival_city: 'Sydney',
        arrival_time: '2023-07-22 18:45',
        passenger_name: 'Emily Brown',
        passenger_gender: 'Female',
        seat_number: 'D4',
        currency: 'JPY',
        departure_gate: 'D5',
        flight_status: 'Cancelled',
        co_pilot_name: 'David Johnson',
        aircraft_type: 'Boeing 777',
        fuel_consumption: 9000.00
      }
    }
  }
]);
```

```mongodb
{
  acknowledged: true,
  insertedCount: 3,
  insertedIds: {
    '0': ObjectId("64d1711863e205aadb7039b6"),
    '1': ObjectId("64d1711863e205aadb7039b7"),
    '2': ObjectId("64d1711863e205aadb7039b8")
  },
  matchedCount: 0,
  modifiedCount: 0,
  deletedCount: 0,
  upsertedCount: 0,
  upsertedIds: {}
}
```

# VALIDAR DOCUMENTOS INSERTADOS
```mongodb
db.vuelos_1.find(
  {
    id:{ $gt:9997 }
  }
)
.count()
```

# ACTUALIZAR MULTIPLES DOCUMENTOS, MULTIPLICADO SU id POR 100
```mongodb
db.vuelos_1.bulkWrite([
  {
    updateMany: {
      filter: { id: { $gt: 9997 } },
      update: { $mul: { id: 100 } }
    }
  }
]);
```

# VALIDAR DOCUMENTOS ACTUALIZADOS
```mongodb
db.vuelos_1.find(
  {id:{$gt:9997}},
  {
    _id: 1,
	 id: 1
  }
)
```

# ELIMINAR MULTIPLES DOCUMENTOS

```mongodb
db.vuelos_1.bulkWrite([
  {
    deleteMany: {
      filter: { id: { $gt: 9997 } }
    }
  }
]);
```

```mongodb
{
  acknowledged: true,
  insertedCount: 0,
  insertedIds: {},
  matchedCount: 0,
  modifiedCount: 0,
  deletedCount: 13,
  upsertedCount: 0,
  upsertedIds: {}
}
```

# INSERCION, ACTUALIZACION Y ELIMINACION, SENCILLA
```mongodb
const bulkOps = [
  // Inserción
  { insertOne: { document: { id: 10006, name: "Documento 10006" } } },

  // Actualización
  { updateOne: { filter: { id: { $gt: 9997 } }, update: { $set: { name: "Actualizado" } } } },

  // Eliminación
  { deleteOne: { filter: { id: { $gt: 9997 } } } }
];

db.collection.bulkWrite(bulkOps);
```

# INSERCION, ACTUALIZACION Y ELIMINACION, MULTIPLE
```mongodb
// Crear el array de operaciones
var bulkOps = [
  { insertOne: { document: { id: 10006, campo: 'valor1' } } },
  { insertOne: { document: { id: 10007, campo: 'valor2' } } },
  { insertOne: { document: { id: 10008, campo: 'valor3' } } },
  { insertOne: { document: { id: 10009, campo: 'valor4' } } },
  { insertOne: { document: { id: 10010, campo: 'valor5' } } },
  { updateMany: { filter: { id: { $gte: 10006, $lte: 10010 } }, update: { $set: { campo: 'nuevo_valor' } } } },
  { deleteMany: { filter: { id: { $gte: 10006, $lte: 10010 } } } }
];

// Ejecutar las operaciones con bulkWrite
db.collection.bulkWrite(bulkOps);

```

# VER EL PLAN DE EJECUCION DE UNA CONSULTA

| Tipo de Explicación           | Descripción                                                                                                                             | Uso                                                  |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| "queryPlanner"                | Proporciona detalles sobre cómo el optimizador de consultas planifica la ejecución de la consulta.                                   | db.collection.find(query).explain("queryPlanner")  |
| "executionStats"              | Ofrece información sobre cómo se ejecutó la consulta, incluidos los tiempos y estadísticas de rendimiento.                         | db.collection.find(query).explain("executionStats")|
| "allPlansExecution"           | Proporciona información sobre todos los planes de ejecución considerados por el optimizador y cómo se ejecutaron.                   | db.collection.find(query).explain("allPlansExecution")|

```mongodb
db.vuelos_1.find({seat_number: 'A1'})
           .limit(2)
           .explain()
```
```mongodb
db.vuelos_1.find({seat_number: 'A1'})
           .limit(2)
           .explain("allPlansExecution")
```

```mongodb
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'test_mongo.vuelos_1',
    indexFilterSet: false,
    parsedQuery: {
      seat_number: {
        '$eq': 'A1'
      }
    },
    queryHash: '3054E2EB',
    planCacheKey: '3054E2EB',
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: {
      stage: 'LIMIT',
      limitAmount: 2,
      inputStage: {
        stage: 'COLLSCAN',
        filter: {
          seat_number: {
            '$eq': 'A1'
          }
        },
        direction: 'forward'
      }
    },
    rejectedPlans: []
  },
  command: {
    find: 'vuelos_1',
    filter: {
      seat_number: 'A1'
    },
    limit: 2,
    '$db': 'test_mongo'
  },
  serverInfo: {
    host: 'Paradigma',
    port: 27017,
    version: '6.0.8',
    gitVersion: '3d84c0dd4e5d99be0d69003652313e7eaf4cdd74'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600
  },
  ok: 1
}
```


# Validación de documentos
```mongodb

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
