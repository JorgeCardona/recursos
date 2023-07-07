# PRUEBA CON CONTENEDORES DE POSTGRES Y MYSQL
| Configuración | PostgreSQL| MySQL                        |
|---------------|-----------|------------------------------|
| Host          | localhost | localhost                    |
| Port          | 5555      | 3333                         |
| User          | admin     | admin                        |
| Password      | 12345678  | 12345678                     |
| Database      | test_poc  | test_poc                     |
| Schema        | public    | test_poc                     |

# Cliente DBeaver para probar las conexiones

# LAS TABLAS EN POSTGRES SON SENSIBLES AL CASO
# Iniciar postgres con docker
```yaml
docker run --name jorgecardona-postgres --rm -e POSTGRES_DB=test_poc -e POSTGRES_PASSWORD=12345678 -e POSTGRES_USER=admin -d -p 5555:5432 postgres:13.11-bullseye
```

# Iniciar mysql con docker
```yaml
docker run --name jorgecardona-mysql --rm -e MYSQL_DATABASE=test_poc -e MYSQL_PASSWORD=12345678 -e MYSQL_USER=admin -e MYSQL_ROOT_PASSWORD=root -d -p 3333:3306 mysql:8.0.33
```

# En la consola de MySQL ejecutar el comando para poder actualizar y eliminar.
```sql
SET SQL_SAFE_UPDATES = 0;
```

# crea el entorno virtual
```bash
jorge@cardona:~$ virtualenv venv
```

# activa el entorno virtual
```bash
jorge@cardona:~$ source venv/bin/activate
```

# instala dbt-core y el conector de MySQL y PostgreSQL
```bash
(venv) jorge@cardona:~$ pip install dbt-mysql
(venv) jorge@cardona:~$ pip install dbt-postgres
```

# listar los comandos de DBT
```yaml
(venv) jorge@cardona:~$ dbt

An ELT tool for managing your SQL transformations and data models. For more documentation on these commands, visit: docs.getdbt.com

Available sub-commands:
  {docs,source,init,clean,debug,deps,list,ls,build,snapshot,run,compile,parse,test,seed,run-operation}
    docs                Generate or serve the documentation website for your project.
    source              Manage your project's sources
    init                Initialize a new DBT project.
    clean               Delete all folders in the clean-targets list (usually the dbt_packages and target directories.)
    debug               Show some helpful information about dbt for debugging. Not to be confused with the --debug option which increases
                        verbosity.
    deps                Pull the most recent version of the dependencies listed in packages.yml
    list (ls)           List the resources in your project
    build               Run all Seeds, Models, Snapshots, and tests in DAG order
    snapshot            Execute snapshots defined in your project
    run                 Compile SQL and execute against the current target database.
    compile             Generates executable SQL from source, model, test, and analysis files. Compiled SQL files are written to the target/
                        directory.
    parse               Parsed the project and provides information on performance
    test                Runs tests on data in deployed models. Run this after `dbt run`
    seed                Load data from csv files into your data warehouse.
    run-operation       Run the named macro with any supplied arguments.

```

# crea un nuevo proyecto DBT
```yaml
(venv) jorge@cardona:~$ dbt init multi_database

# define el conector a usar
Enter a number: 
Which database would you like to use?
[1] mariadb
[2] mysql
[3] mysql5
[4] postgres
```

# ir al directorio del proyecto DBT
```bash
(venv) jorge@cardona:~$ cd .\dbt init multi_database\
```
# DIRECTORIODE UN PROYECTO DBT
```
📦 multi_database [project_directory]
┗ 📂 analyses [package]
┗ 📂 dbt_packages [package]
┗ 📂 logs [package]
┗ 📂 macros [package]
┗ 📂 models [package]
┗ 📂 seeds [package]
┗ 📂 snapshots [package]
┗ 📂 target [package]
┗ 📂 test [package]
┗ 📜 dbt_project.yml
┗ 📜 README.md
┗ ⚠️ .gitignore
```

# ver el yaml de configuracion
```bash
(venv) jorge@cardona:~$ ~/.dbt/profiles.yml
```

# EJEMPLO DE profiles.yaml
```yaml
multi_database:
  target: dev
  outputs:
    prod:
      type: mysql
      server: localhost
      port: 3333  # optional
      database: test_poc
      schema: test_poc
      username: admin
      password: '12345678' # las claves deben estar entre comillas
      driver: MySQL ODBC 8.0 ANSI Driver
    dev:
      type: postgres
      threads: 1
      host: localhost
      port: 5555
      user: admin
      pass: '12345678'
      dbname: test_poc
      schema: public
```

# probar la conexion a la base de datos
```yaml
(venv) jorge@cardona/multi_database:~$ dbt debug

23:04:18  Running with dbt=1.5.2
23:04:18  dbt version: 1.5.2
23:04:18  python version: 3.9.2rc1
23:04:18  python path: C:\dbt_venv\venv\Scripts\python.exe
23:04:18  os info: Windows-10-10.0.19041-SP0
23:04:18  Using profiles.yml file at C:\Users\QiDimMak\.dbt\profiles.yml
23:04:18  Using dbt_project.yml file at C:\dbt_venv\multi_database\dbt_project.yml
23:04:18  Configuration:
23:04:18    profiles.yml file [OK found and valid]
23:04:18    dbt_project.yml file [OK found and valid]
23:04:18  Required dependencies:
23:04:18   - git [OK found]

23:04:18  Connection:
23:04:18    host: localhost
23:04:18    port: 5555
23:04:18    user: admin
23:04:18    database: test_poc
23:04:18    schema: public
23:04:18    search_path: None
23:04:18    keepalives_idle: 0
23:04:18    sslmode: None
23:04:18  Registered adapter: postgres=1.5.2
23:04:18    Connection test: [OK connection ok]
```

# usar un archivo .csv para crear una tabla con datos a partir de este archivo
```yaml
(venv) jorge@cardona/multi_database:~$ dbt seed

23:38:17  Running with dbt=1.5.2
23:38:17  Registered adapter: postgres=1.5.2
23:38:17  Found 2 models, 4 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 0 sources, 0 exposures, 0 metrics, 0 groups
23:38:18
23:38:18  Concurrency: 1 threads (target='dev')
23:38:18
23:38:18  1 of 1 START seed file public.FLIGHT_LOGS ...................................... [RUN]
23:39:28  1 of 1 OK loaded seed file public.flight_logs .................................. [INSERT 5000 in 70.82s]
23:39:28  
23:39:29  Finished running 1 seed in 0 hours 1 minutes and 10.99 seconds (70.99s).
23:39:29
23:39:29  Completed successfully
23:39:29  
23:39:29  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```

# Probar la tabla y datos creados con la SEED 
<img src="imagenes\seed_postgres.png">

# CREAR VISTAS Y TABLAS A PARTIR DE MODELOS

# DIRECTORIO DE UN MODELO DE DATOS
```
📦 multi_database [project_directory]
┗ 📂 analyses [package]
┗ 📂 dbt_packages [package]
┗ 📂 logs [package]
┗ 📂 macros [package]
┗ 📂 models [package]
┃ ┣ 📂 src
┃ ┃ ┣ 🌌 postgres_tabla_query_directo_flight_logs.sql
┗ 📂 seeds [package]
┗ 📂 snapshots [package]
┗ 📂 target [package]
┗ 📂 test [package]
┗ 📜 dbt_project.yml
┗ 📜 README.md
┗ ⚠️ .gitignore
```

# CREAR EL PRIMER MODELO
### dentro de la carpeta models crear una carpeta src y el archivo sql y adicionar el codigodel ejemplo 
```
models/postgres_tabla_query_directo_flight_logs.sql
```

# CREAR UNA TABLA
## EJEMPLO POSTGRES
```sql
{{ 
config(
		materialized='table', 
		sort='flight_number', 
		dist='id'
		) 
}}

SELECT id,
		flight_number, 
		airline, 
		departure_airport,
		departure_city, 
		departure_country
FROM test_poc.public."FLIGHT_LOGS"
ORDER BY flight_number
```
# CREAR LA TABLA
```yaml
(venv) jorge@cardona/multi_database:~$ dbt run

00:19:17  Running with dbt=1.5.2
00:19:17  Registered adapter: postgres=1.5.2
00:19:17  [WARNING]: Configuration paths exist in your dbt_project.yml file which do not apply to any resources.
There are 1 unused configuration paths:
- models.multi_database.example
00:19:17  Found 1 model, 0 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 0 sources, 0 exposures, 0 metrics, 0 groups
00:19:17
00:19:17  Concurrency: 1 threads (target='dev')
00:19:17
00:19:17  1 of 1 START sql table model public.postgres_tabla_query_directo_flight_logs ... [RUN]
00:19:17  1 of 1 OK created sql table model public.postgres_tabla_query_directo_flight_logs  [SELECT 5000 in 0.15s]
00:19:17
00:19:17  Finished running 1 table model in 0 hours 0 minutes and 0.33 seconds (0.33s).
00:19:17
00:19:17  Completed successfully
00:19:17
00:19:17  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```
<img src="imagenes\tabla_postgres.png">

# CREAR UNA VISTA Y USAR UN MODELO DE REFERENCIA
### usando el archivo sql creado anteriormente 'postgres_tabla_query_directo_flight_logs'

# DIRECTORIO DE UN MODELO DE DATOS
```
📦 multi_database [project_directory]
┗ 📂 analyses [package]
┗ 📂 dbt_packages [package]
┗ 📂 logs [package]
┗ 📂 macros [package]
┗ 📂 models [package]
┃ ┣ 📂 src
┃ ┃ ┣ 🌌 postgres_tabla_query_directo_flight_logs.sql
┃ ┃ ┣ 🌌 postgres_vista_query_con_with_y_referencia.sql
┗ 📂 seeds [package]
┗ 📂 snapshots [package]
┗ 📂 target [package]
┗ 📂 test [package]
┗ 📜 dbt_project.yml
┗ 📜 README.md
┗ ⚠️ .gitignore
```

### dentro de la carpeta models crear una carpeta src y el archivo sql y adicionar el codigodel ejemplo 
```
models/postgres_vista_query_con_with_y_referencia.sql
```

## EJEMPLO POSTGRES
```sql
-- alias de tabla a consultar
WITH SELECT_TEST AS(

SELECT * FROM {{ ref('postgres_tabla_query_directo_flight_logs') }}
)

--- select que crea la vista
SELECT flight_number, 
		airline, 
		departure_airport,
		departure_city, 
		departure_country
FROM SELECT_TEST
```
# CREAR LA VISTA
```yaml
(venv) jorge@cardona/multi_database:~$ dbt run

00:34:08  Running with dbt=1.5.2
00:34:08  Registered adapter: postgres=1.5.2
00:34:08  [WARNING]: Configuration paths exist in your dbt_project.yml file which do not apply to any resources.
There are 1 unused configuration paths:
- models.multi_database.example
00:34:08  Found 2 models, 0 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 3 sources, 0 exposures, 0 metrics, 0 groups
00:34:08  
00:34:08  Concurrency: 1 threads (target='dev')
00:34:08  
00:34:08  1 of 2 START sql table model public.postgres_tabla_query_directo_flight_logs ... [RUN]
00:34:08  1 of 2 OK created sql table model public.postgres_tabla_query_directo_flight_logs  [SELECT 5000 in 0.15s]
00:34:08  2 of 2 START sql view model public.postgres_vista_query_con_with_flight_logs ... [RUN]
00:34:08  2 of 2 OK created sql view model public.postgres_vista_query_con_with_flight_logs  [CREATE VIEW in 0.08s]
00:34:08  
00:34:08  Finished running 1 table model, 1 view model in 0 hours 0 minutes and 0.41 seconds (0.41s).
00:34:08  
00:34:08  Completed successfully
00:34:08
00:34:08  Done. PASS=2 WARN=0 ERROR=0 SKIP=0 TOTAL=2
```
<img src="imagenes\vista_postgres_referencia.png">


# CREAR UNA NUEVA VISTA CON JOINS, USANDO FUENTES
# DIRECTORIO DE FUENTES DE DATOS
```
📦 multi_database [project_directory]
┗ 📂 analyses [package]
┗ 📂 dbt_packages [package]
┗ 📂 logs [package]
┗ 📂 macros [package]
┗ 📂 models [package]
┃ ┃ 🌻 sources.yaml
┃ ┣ 📂 src
┃ ┃ ┣ 🌌 postgres_tabla_query_directo_flight_logs.sql
┃ ┃ ┣ 🌌 postgres_vista_query_con_with_y_referencia.sql
┃ ┃ ┣ 🌌 mysql_vista_query_directo_con_source_y_join.sql
┗ 📂 seeds [package]
┗ 📂 snapshots [package]
┗ 📂 target [package]
┗ 📂 test [package]
┗ 📜 dbt_project.yml
┗ 📜 README.md
┗ ⚠️ .gitignore
```
# PARA USAR MYSQL CAMBIAR target=prod

```yaml
multi_database:
  target: prod
  outputs:
    prod:
      type: mysql
      server: localhost
      port: 3306  # optional
      database: test_poc
      schema: test_poc
      username: root
      password: '12345678' # las claves deben estar entre comillas
      driver: MySQL ODBC 8.0 ANSI Driver
    dev:
      type: postgres
      threads: 1
      host: localhost
      port: 5555
      user: admin
      pass: '12345678'
      dbname: test_poc
      schema: public
```
# EJEMPLO DE sources.yaml

```yaml
version: 2

sources:
  - name: fuente_original
    description: Fuente de datos original creada con el csv
    schema: test_poc
    database: test_poc

    freshness: # si se ubica antes de las tablas aplica para todas las tablas
      warn_after:
        count: 1
        period: minute # si en este tiempo 1 minuto no hay nuevos registros y actualizada la columna de timestamp 'test_time_freshness' muestra la alerta
      error_after:
        count: 3
        period: minute  # si en este tiempo 3 minutos no hay nuevos registros y actualizada la columna de timestamp 'test_time_freshness' muestra el error      

    tables:
      - name: tabla_original # se puede usar como un alias en la source
        identifier: flight_logs # debe ser el nombrede la tabla en la base de datos
        # cmapo que sirve para probar que tan a menudo se actualiza la tabla 
        loaded_at_field: test_time_freshness # tiene que ser un campo TIMESTAMP de la tabla para el freshness 

  - name: tabla_referencia
    description: Fuente de datos de clientes
    schema: test_poc
    database: test_poc
    tables:
       - name: clientes_alias # se puede usar como un alias en la source
         identifier: tabla_query_directo_flight_logs # debe ser el nombrede la tabla en la base de datos

  - name: vista_referencia
    description: Fuente de datos de órdenes
    schema: test_poc
    database: test_poc
    tables:
      - name: vista_query_con_with_flight_logs
        quoting: 
          identifier: true
```
# PROBAR freshness
## SE TRATA DE VALIDAR QUE LOS DATOS DE LA FUENTE DE DATOS SE ESTE ACTUALIZANDO PERIODICAMENTE EN EL TIEMPO DETERMINADO, SINO MUESTRA UN **WARNING** O **ERROR** SEGUN EL CASO

# ADICIONA UNA COLUMNA TIMESTAMP PARA HACER LA PRUEBA
```sql
ALTER TABLE test_poc.flight_logs 
ADD COLUMN test_time_freshness TIMESTAMP NULL DEFAULT now();
```

# VALIDANDO SIN QUE PASE EL INTERVALO INICIAL DE 1 MINUTO
```yaml
(venv) jorge@cardona/multi_database:~$ dbt source freshness

05:16:01  Found 4 models, 0 tests, 2 snapshots, 0 analyses, 172 macros, 0 operations, 2 seed files, 3 sources, 0 exposures, 0 metrics
05:16:01
05:16:01  Concurrency: 1 threads (target='prod')
05:16:01
05:16:01  1 of 1 START freshness of fuente_original.tabla_original ....................... [RUN]
05:16:01  1 of 1 PASS freshness of fuente_original.tabla_original ........................ [PASS in 0.04s]
```

# VALIDANDO WARNINGS, YA PASO 1 MINUTO
```yaml
(venv) jorge@cardona/multi_database:~$ dbt source freshness

05:04:57  Found 4 models, 0 tests, 2 snapshots, 0 analyses, 172 macros, 0 operations, 2 seed files, 3 sources, 0 exposures, 0 metrics
05:04:57
05:04:57  Concurrency: 1 threads (target='prod')
05:04:57  
05:04:57  1 of 1 START freshness of fuente_original.tabla_original ....................... [RUN]
05:04:57  1 of 1 WARN freshness of fuente_original.tabla_original ........................ [WARN in 0.04s]
05:04:57  Done.
```

# VALIDANDO ERRORES, YA PASARON 2 MINUTOS
```yaml
(venv) jorge@cardona/multi_database:~$ dbt source freshness

05:04:40  Concurrency: 1 threads (target='prod')
05:04:40
05:04:40  1 of 1 START freshness of fuente_original.tabla_original ....................... [RUN]
05:04:40  1 of 1 ERROR STALE freshness of fuente_original.tabla_original ................. [ERROR STALE in 0.04s]
05:04:40
```

# INSERTANDO NUEVOS DATOS
```sql
INSERT INTO test_poc.flight_logs
VALUES ('7777', '01H4EEMMVWTD0QNCNHCWDQ7Y40', '2014', '2309', 'United', 'RST', 'Gabriela Zea', 'Colombia', '2022-03-30', '2023-07-07 14:14:22', 'CRY', 'Kaseda-shirakame', 'Japan', '26-1-2022', '2023-07-06 00:46:28', '5.55', 'Rici Preon', '8', 'Female', 'China', 'C3', '501.04', 'DOP', '43.15', 'B2', 'F6', 'Departed', 'Carolee Bonett', 'Adriena Burbury', '7', 'Boeing 737', 'N12345', '2884.71', '3647.15', now());
```
# VALIDANDO SIN QUE PASE EL INTERVALO INICIAL DE 1 MINUTO
```yaml
(venv) jorge@cardona/multi_database:~$ dbt source freshness

05:16:01  Found 4 models, 0 tests, 2 snapshots, 0 analyses, 172 macros, 0 operations, 2 seed files, 3 sources, 0 exposures, 0 metrics
05:16:01
05:16:01  Concurrency: 1 threads (target='prod')
05:16:01
05:16:01  1 of 1 START freshness of fuente_original.tabla_original ....................... [RUN]
05:16:01  1 of 1 PASS freshness of fuente_original.tabla_original ........................ [PASS in 0.04s]
```

### dentro de la carpeta models crear una carpeta src y el archivo sql y adicionar el codigodel ejemplo 
```
models/postgres_vista_query_directo_con_source.sql
```

## EJEMPLO MYSQL
```sql
SELECT t1.*
FROM {{ source('tabla_referencia','clientes_alias') }} AS t1
JOIN {{ source('vista_referencia','vista_query_con_with_flight_logs') }} AS t2
  ON t1.flight_number = t2.flight_number
WHERE t1.id > 1500 AND t1.id < 1800
```

<img src="imagenes\vista_mysql_source_join.png">

### dentro de la carpeta models crear una carpeta src y el archivo sql y adicionar el codigo del ejemplo 
```
models/vista_con_nombre_personalizado.sql
```
# EJEMPLO MYSQL
```sql
{{
  config(
    materialized='view',
    alias='nombre_personalizado'
  )
}}

# alias de tabla a consultar
WITH SELECT_TEST AS(

SELECT * FROM {{ ref('tabla_query_directo_flight_logs') }}
)

# select que crea la vista
SELECT flight_number, 
		airline, 
		departure_airport,
		departure_city, 
		departure_country
FROM SELECT_TEST
```
<img src="imagenes\vista_mysql_con_nombre_personalizado.png">

# SNAPSHOT

```sql
-- target_database='dbt_snapshots'
-- target_schema='dbt_snapshots'
{% snapshot validar_multi_campos_snapshot %}

{{
  config(
    target_database='dbt_snapshots',
    target_schema='dbt_snapshots',
    unique_key='id',
    strategy='check',
    invalidate_hard_deletes=True,
    check_cols=['flight_number', 'airline']
  )
}}

SELECT
  id,
  secure_code,
  flight_number,
  airline,
  departure_airport
FROM {{ source('fuente_original','tabla_original') }}
WHERE id = 1

{% endsnapshot %}
```

---

```sql
-- si no existe la base de datos o las tablas, las crea.
-- target_database='dbt_snapshots_todos_los_campos'
-- target_schema='dbt_snapshots_todos_los_campos'
{% snapshot validar_todos_los_campos_snapshot %}

{{
  config(
    target_database='dbt_snapshots_todos_los_campos',
    target_schema='dbt_snapshots_todos_los_campos',
    unique_key='id',
    strategy='check',
    invalidate_hard_deletes=True,
    check_cols='all'
  )
}}

SELECT
  id,
  secure_code,
  flight_number,
  airline,
  departure_airport
FROM {{ source('fuente_original','tabla_original') }}
WHERE id = 1

{% endsnapshot %}
```

# EJECUTAR EL SNAPSHOT
```
(venv) jorge@cardona/multi_database:~$ dbt snapshot
```
<img src="imagenes\snapshot_mysql.png">

# MODIFICAR UN REGISTRO
<img src="imagenes\snapshot_mysql_secure_code.png">

# EJECUTAR EL SNAPSHOT
```
(venv) jorge@cardona/multi_database:~$ dbt snapshot
```
<img src="imagenes\snapshot_mysql_secure_code_completado.png">

# MODIFICAR UN REGISTRO
<img src="imagenes\snapshot_mysql_flight_number.png">

# EJECUTAR EL SNAPSHOT
```
(venv) jorge@cardona/multi_database:~$ dbt snapshot
```
<img src="imagenes\snapshot_mysql_flight_number_completado.png">


# ALGUNAS COSAS NO FUNCIONAN BIEN EN LOS CONTENEDORES DE DOCKER Y POSTGRES COMO LOS SNAPSHOT LOS QUERIES CON JOIN
# LOS QUERIES NO DEBEN TERMINAR EN punto y coma ; generan errores

# Detener Contenedor postgres
```
docker stop jorgecardona-postgres
```

# Detener Contenedor mysql
```
docker stop jorgecardona-mysql
```

