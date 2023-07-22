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


# ACCEDER A LA CONSOLA DE MONGO DENTRO DE MONGODB COMPASS
<img src="imagenes\00_mongosh.png">

# CREAR UN USUARIO

```sql
local > use admin
db.createUser({
   user: "mongodb",
   pwd: "12345678",
   roles: ["root"]
})

{ ok: 1 }
```

# LISTAR USUARIOS

```sql
admin > show users
[
  {
    _id: 'admin.mongodb',
    userId: UUID("ab914c24-b538-4a73-b9e1-5895137dee64"),
    user: 'mongodb',
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
  }
]
```

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

# HACER UN JOIN **lookup** ENTRE 2 COLECCIONES Y TRAER SOLO EL PRIMER DOCUMENTO '$limit: 1'

```sql
# Join two collections using $lookup operator
test_mongo > 
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

```sql
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

# SI QUIERE TENER LOS VALORES SIN ANIDAR UNA DE LAS COLECCIONES
# PRIMERO LOS CAMPOS DE LA PRIMERA COLECCION

```sql
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
```sql
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

```sql
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
```sql
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
```sql
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
```sql
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