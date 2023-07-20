# EMOJIS
# https://es.piliapp.com/emoji/list/
# Contenido
 - [Crear un entorno virtual](#crear-un-entorno-virtual)
 - [Activar el entorno virtual](#activar-el-entorno-virtual)
 - [Instalar DBT y el adapatador a base de datos](#instalacion-de-dbt-core-y-el-conector-postgresql)
 - [Validar version de DBT](#verificar-version-dbt) 
 - [Listar los comandos de DBT](#listar-los-comandos-de-dbt)
 - [Crear un proyecto DBT](#crear-un-proyecto-dbt)
 - [Estructura de un proyecto DBT](#estructura-de-un-proyecto-dbt)
 - [Descripcion de los directorios y archivos en un proyecto DBT](#descripcion-de-los-directorios-y-archivos-de-un-proyecto-dbt)
 - [Acceder al yaml de configuracion de Perfiles](#acceder-al-yaml-de-configuracion-de-perfiles)
 - [Probar la conexion a la base de datos desde DBT](#probar-la-conexion-a-la-base-de-datos-desde-dbt)
 - [Poblar la base de datos usando un archivo CSV](#poblar-la-base-de-datos-usando-un-archivo)
 - [Crear el primer modelo una vista](#crear-el-primer-modelo-una-vista)
 - [Crear el segundo modelo una tabla](#crear-el-segundo-modelo-una-tabla)
 - [Crear el tercer una tabla con nombre personalizado, usando una tabla temporal](#crear-el-tercer-modelo-una-tabla-con-nombre-personalizado-alias-y-con-una-tabla-temporal-usando-with)
 - [Adicionar columna TIMESTAMP para probar el freshness](#adicionar-columna-timestamp-para-probar-el-freshness)

## Crear un entorno virtual
```yaml
jorge@cardona:~$ pip install virtualenv

jorge@cardona:~$ virtualenv venv
```

### Activar el entorno virtual
```yaml
# linux
jorge@cardona:~$ source venv/bin/activate
(venv) jorge@cardona:~$

# windows
jorge@cardona:~$ venv/Scripts/activate
(venv) jorge@cardona:~$
```

## Instalacion de dbt-core y el conector PostgreSQL
```yaml
(venv) jorge@cardona:~$ pip install dbt-core
(venv) jorge@cardona:~$ pip install dbt-postgres
```

## Verificar Version DBT
```yaml
(venv) jorge@cardona:~$ dbt --version

Core:
  - installed: 1.5.2
  - latest:    1.5.2 - Up to date!

Plugins:
  - postgres: 1.5.2 - Up to date!
```

# Listar los comandos de DBT
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

# Crear un proyecto DBT
```yaml
(venv) jorge@cardona:~$ dbt init dbt_poc

# define el conector a usar
Enter a number: 
Which database would you like to use?
[1] postgres

Enter a number: 1
Your new dbt project "dbt_poc" was created!
Happy modeling!
```

# Estructura de un proyecto DBT
```
⭐ dbt_poc [project_directory]
┗ ☢️ analyses [package]
  ┗ 📍.gitkeep
┗ 🦄 macros [package]
  ┗ 📍.gitkeep
┗ 🌞 models [package]
  ┗ ⚜️ schema.yml
  ┗ ♻️ sources.yml
┗ 🌼 seeds [package]
  ┗ 📍.gitkeep
┗ 📸 snapshots [package]
  ┗ 📍.gitkeep
┗ 🚀 test [package]
  ┗ 📍.gitkeep
┗ 🔎 logs [package]
  ┗ 👀 dbt.log
┗ 🔑 dbt_project.yml
┗ 🎁 README.md
┗ ⛔.gitignore
┗ 🛒 dbt_packages [package]
┗ 🎯 target [package]
┗ ❄️ assets [package] creado 
```

# Descripcion de los directorios y archivos de un proyecto DBT

Aquí tienes la tabla actualizada, incluyendo los archivos faltantes:

| Archivo/Directorio      | Función                                                     | Descripción                                                                                                                             |
|----------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| dbt_poc              | Directorio principal del proyecto dbt                        | Directorio raíz del proyecto dbt                                                                                                        |
| ┗ analyses           | Carpeta que contiene los archivos .sql con análisis (queries) de datos, que representan los análisis de datos realizados en el proyecto.  | Cualquier .sql dentro de este directorio, se compilará, pero no se ejecutará.  |
| ┗ macros             | Carpeta que contiene macros personalizados                   | Contiene los archivos .sql con macros reutilizables que pueden ser invocados en los modelos y análisis                                 |
| ┗ models             | Carpeta que contiene los modelos de datos                    | Contiene los archivos .sql que representan los modelos de datos utilizados para transformar y combinar los datos de origen                |
| ┗ ┗ schema.yml        | Archivo que define la estructura del esquema de los modelos  | Archivo YAML que describe la estructura del esquema de los modelos de datos                                                              |
| ┗ ┗ sources.yml       | Archivo que define las fuentes de datos de los modelos       | Archivo YAML que especifica las fuentes de datos utilizadas por los modelos de datos                                                    |
| ┗ seeds              | Carpeta que contiene datos de prueba (seeds)                 | Contiene los archivos .csv o .json que proporcionan datos iniciales de prueba para el desarrollo y las pruebas de los modelos de dbt       |
| ┗ snapshots          | Carpeta que contiene instantáneas de los modelos de datos    | Contiene los archivos .sql que representan instantáneas (cachés) de los modelos de datos para un acceso más rápido y eficiente             |
| ┗ test               | Carpeta que contiene pruebas para los modelos                | Contiene los archivos .sql que representan las pruebas unitarias y de integración para los modelos de datos                             |
| ┗ logs               | Carpeta que contiene los registros de ejecución de dbt       | Contiene el archivo dbt.log que registra los detalles y resultados de las ejecuciones de dbt                                          |
| ┗ dbt_project.yml    | Archivo de configuración principal de dbt                    | Archivo YAML que contiene la configuración del proyecto dbt, incluyendo las conexiones a bases de datos, variables y configuraciones de dbt |
| ┗ README.md          | Archivo de documentación del proyecto                        | Archivo de texto que proporciona información y descripción general del proyecto dbt                                                     |
| ┗ .gitignore         | Archivo que especifica los archivos/directorios ignorados por Git | Archivo que indica a Git qué archivos y directorios debe ignorar durante el control de versiones                                        |
| ┗ dbt_packages       | Carpeta que puede contener paquetes externos de dbt          | Carpeta opcional para almacenar paquetes externos de dbt, que pueden ser utilizados en el proyecto                                    |
| ┗ target             | Carpeta que contiene los archivos generados por dbt          | Carpeta donde se generan los archivos resultantes de las transformaciones y cargas de datos realizadas por dbt                          |
| ┗ .gitkeep           | Archivo de marcador                                          | El archivo `.gitkeep` se utiliza para mantener los directorios vacíos dentro del control de versiones de Git.                           |


# ir al directorio del proyecto DBT
```bash
(venv) jorge@cardona:~$ cd dbt_poc
```

# Acceder al yaml de configuracion de perfiles
```yaml
(venv) jorge@cardona/dbt_poc:~$ ~/.dbt/profiles.yml
```

# EJEMPLO DE profiles.yaml
```yaml
dbt_poc:
  target: dev
  outputs:
    dev:
      type: postgres
      threads: 1
      host: localhost
      port: 5432
      user: postgres
      pass: '12345678'
      dbname: postgres
      schema: public
```

# Probar la conexion a la base de datos desde DBT
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt debug

04:43:41  Running with dbt=1.5.2
04:43:41  Configuration:
04:43:41    profiles.yml file [OK found and valid]
04:43:41    dbt_project.yml file [OK found and valid]
04:43:41  Required dependencies:
04:43:41   - git [OK found]

04:43:41  Connection:
04:43:41    host: localhost
04:43:41    port: 5432
04:43:41    user: postgres
04:43:41    database: postgres
04:43:41    schema: public
04:43:41    search_path: None
04:43:41    keepalives_idle: 0
04:43:41    sslmode: None
04:43:41  Registered adapter: postgres=1.5.2
04:43:42    Connection test: [OK connection ok]

04:43:42  All checks passed!
```

# Poblar la base de datos usando un archivo

```yaml
Adicionar el archivo flight_logs.csv dentro de la carpeta SEEDS
```
```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
```
```yaml
# dbt seed --show permite ver un random example de los datos del seed
# dbt seed ejecuta el poblado de datos sin preview
(venv) jorge@cardona/dbt_poc:~$ dbt seed --show

23:38:17  Running with dbt=1.5.2
23:38:17  Registered adapter: postgres=1.5.2
23:38:17  Found 0 models, 0 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 0 sources, 0 exposures, 0 metrics, 0 groups
23:38:18  Concurrency: 1 threads (target='dev')
23:38:18  1 of 1 START seed file public.FLIGHT_LOGS ...................................... [RUN]
23:39:28  1 of 1 OK loaded seed file public.flight_logs .................................. [INSERT 5000 in 70.82s]
23:39:29  Finished running 1 seed in 0 hours 1 minutes and 10.99 seconds (70.99s).
23:39:30  Random sample of table: public.flight_logs
23:39:30 ------------------------------------------
|    id | secure_code          | flight_id | flight_number | airline  | departure_airport | departure_city | departure_country | departure_date |      departure_time | arrival_airport | arrival_city | arrival_country | arrival_date |        arrival_time | flight_duration | passenger_name     | passenger_age | passenger_gender | passenger_nationa... | seat_number | ticket_price | currency | baggage_weight | departure_gate | arrival_gate 
| flight_status | pilot_name         | co_pilot_name    | cabin_crew_count | aircraft_type | aircraft_registra... | fuel_consumption | flight_distance |
| ----- | -------------------- | --------- | ------------- | -------- | ----------------- | -------------- | ----------------- | -------------- | ------------------- | --------------- | ------------ | --------------- | ------------ | ------------------- | --------------- | ------------------ | ------------- | ---------------- | -------------------- | ----------- | ------------ | -------- | -------------- | -------------- | ------------ 
| ------------- | ------------------ | ---------------- | ---------------- | ------------- | -------------------- | ---------------- | --------------- |
| 3,430 | 01H4EEMWYE4HC82Y7... |     3,430 |         1,430 | United   | SOD               | Shimiaozi      | China             |     2022-11-25 | 2023-07-06 16:29:56 | VMU             | Bayog        | Philippines     | 5-10-2022    | 2023-07-06 08:02:19 |           22.14 | Byram Booth        |            33 | Male             | Indonesia            | B2          |       480.64 | CNY      |          21.52 | C3             | F6
| On Time       | Martainn Payfoot   | Warde Sleford    |                2 | Embraer E190  | N12345               |         2,104.68 |        4,823.04 |
| 2,868 | 01H4EEMV833E8RQQ8... |     2,868 |         5,640 | American | MIM               | Cartago        | Colombia          |     2022-11-18 | 2023-07-06 19:15:12 | MBP             | Bolou        | Indonesia       | 4-7-2022     | 2023-07-06 00:12:07 |           22.60 | Ebony Navarro      |            18 | Non-binary       | Togo                 | C3          |       710.09 | COP      |          22.89 | B2             | F6
| Cancelled     | Yoko Born          | Aurlie O'Sheils  |                8 | Embraer E190  | N67890               |         7,892.16 |        3,247.37 |
|   ... | ...                  |       ... |           ... | ...      | ...               | ...            | ...               |            ... |                 ... | ...             | ...          | ...             | ...          |
  ... |             ... | ...                |           ... | ...              | ...                  | ...         |          ... | ...      |            ... | ...            | ...          | ...           | ...                | ...
|              ... | ...           | ...                  |              ... |             ... |
23:39:30  Completed successfully
23:39:30  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```
# Probar la tabla y datos creados con la SEED 
<img src="imagenes\poblado_seed.png">

# Adicionar columna TIMESTAMP para probar el freshness
```sql
ALTER TABLE postgres.public.flight_logs 
ADD COLUMN test_time_freshness TIMESTAMP NULL DEFAULT now();
```
<img src="imagenes\freshness_adicionar_columna.png">

# MODELOS

Un modelo en dbt es como un plano o una receta para transformar datos. Imagina que tienes un montón de ingredientes y necesitas convertirlos en algo delicioso, como una pizza. Para hacerlo, sigues una receta paso a paso que te indica cómo mezclar los ingredientes, amasar la masa, agregar los toppings y hornearla.

En dbt, un modelo es similar a esa receta. Es un conjunto de instrucciones que te dicen cómo tomar datos de una fuente (como una base de datos) y transformarlos en algo útil. Los modelos de dbt te ayudan a realizar operaciones como filtrar datos, agregar cálculos o combinar información de diferentes tablas. Son como las instrucciones que sigues para crear algo nuevo y útil con tus datos.

En resumen, un modelo en dbt es como una receta que te dice cómo transformar datos para obtener información valiosa. Es una manera de organizar y estructurar los datos para que puedas analizarlos y tomar decisiones basadas en ellos.

# TIPOS DE MODELO
| Materialización | Descripción                                                  | Ejemplo de Implementación en dbt                                                                                                                               |
|-----------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Table           | Crea una tabla física en la base de datos.                   | {{config(materialized='table')}}
| View            | Crea una vista virtual en la base de datos.                   | {{config(materialized='view')}} |
| Incremental     | Actualiza solo las filas modificadas desde la última ejecución. | {{config(materialized='incremental')}}                   |
| Snapshot        | Crea una tabla que almacena instantáneas de datos en un momento específico. | {{config(materialized='snapshot')}} |
| Ephemeral       | Genera los resultados de manera dinámica cada vez que se consulta el modelo. | {{config(materialized='ephemeral')}} |

# CREAR **UNA VISTA** COMO PRIMER MODELO 
## dentro de la carpeta models crear una carpeta src
### dentro de la carpeta src crear un archivo sql y adicionar el codigo del ejemplo 
```
models/src/modelo_1_vista_query_directo.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
```
## EJEMPLO guardando algunas columnas en la SINK
```sql
SELECT 
      id,
      flight_number, 
      airline, 
      departure_airport,
      departure_gate,
      departure_city, 
      departure_country
FROM public.flight_logs
ORDER BY flight_number
```

# CREAR LA VISTA
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt run

- models.dbt_poc.example
01:35:05  Found 1 model, 0 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 0 sources, 0 exposures, 0 metrics, 0 groups
01:35:05
01:35:05  Concurrency: 1 threads (target='dev')
01:35:05  
01:35:05  1 of 1 START sql view model public.modelo_1_vista_query_directo ................ [RUN]
01:35:06  1 of 1 OK created sql view model public.modelo_1_vista_query_directo ........... [CREATE VIEW in 0.17s]
01:35:06  
01:35:06  Finished running 1 view model in 0 hours 0 minutes and 0.45 seconds (0.45s).
01:35:06
01:35:06  Completed successfully
01:35:06
01:35:06  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```

# Comprobar el modelo creado
<img src="imagenes\modelo_1.png">

# CREAR **UNA TABLA** COMO SEGUNDO MODELO 
### dentro de la carpeta src crear un archivo sql y adicionar el codigo del ejemplo 
```
models/src/modelo_2_tabla_query_con_with_renombrando_columnas.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
```
## EJEMPLO TABLA, renombrando la columnas y guardandolas con este nombre en la SINK
```sql
{{
  config(
    materialized='table',
    sort='flight_number',
    dist='id'
    ) 
}}

WITH EJEMPLO_SELECT_WITH AS (
  SELECT
    id AS ID,
    flight_number AS FLIGHT_CODE,
    airline AS CARRIER,
    departure_airport AS ORIGINATING_AIRPORT,
    departure_gate AS BOARDING_GATE,
    departure_city AS ORIGINATING_CITY,
    departure_country AS ORIGINATING_COUNTRY
  FROM public.flight_logs
)

SELECT * 
FROM EJEMPLO_SELECT_WITH
ORDER BY FLIGHT_CODE
```

# CREAR LA TABLA
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt run

- models.dbt_poc.example
01:34:07  Found 2 models, 0 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 0 sources, 0 exposures, 0 metrics, 0 groups
01:34:07
01:34:07  Concurrency: 1 threads (target='dev')
01:34:07  
01:34:07  1 of 2 START sql view model public.modelo_1_vista_query_directo ................ [RUN]
01:34:07  1 of 2 OK created sql view model public.modelo_1_vista_query_directo ........... [CREATE VIEW in 0.16s]
01:34:07  2 of 2 START sql table model public.modelo_2_tabla_query_con_with_renombrando_columnas  [RUN]
01:34:07  2 of 2 OK created sql table model public.modelo_2_tabla_query_con_with_renombrando_columnas  [SELECT 5000 in 0.14s]
01:34:08  
01:34:08  Finished running 1 view model, 1 table model in 0 hours 0 minutes and 0.55 seconds (0.55s).
01:34:08
01:34:08  Completed successfully
01:34:08
01:34:08  Done. PASS=2 WARN=0 ERROR=0 SKIP=0 TOTAL=2
```
# Comprobar el modelo creado
<img src="imagenes\modelo_2.png">

# CREAR UNA **TABLA CON NOMBRE PERSONALIZADO** COMO TERCER MODELO ALIAS Y CON UNA TABLA TEMPORAL USANDO WITH
### dentro de la carpeta src crear un archivo sql y adicionar el codigo del ejemplo 
```
models/src/modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
```

# Estrategias incrementales admitidas por adaptador
| data platform adapter | default strategy | additional supported strategies   |
|-----------------------|------------------|-----------------------------------|
| dbt-postgres          | append           | delete+insert                     |
| dbt-redshift          | append           | delete+insert                     |
| dbt-bigquery          | merge            | insert_overwrite                  |
| dbt-spark             | append           | merge (Delta only) insert_overwrite |
| dbt-databricks        | append           | merge (Delta only) insert_overwrite |
| dbt-snowflake         | merge            | append, delete+insert             |
| dbt-trino             | append           | merge delete+insert               |

La estrategia merge está disponible en dbt-postgres y dbt-redshift a partir de dbt v1.6.

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
```
## EJEMPLO TABLA INCREMENTAL, renombrando la columnas y guardandolas con este nombre en la SINK
```sql
{{
  config(
    materialized='incremental',
    alias='tabla_incremental'
    ) 
}}

WITH SELECT_TEST AS (
    SELECT * FROM {{ ref('modelo_2_tabla_query_con_with_renombrando_columnas') }}
)

SELECT * FROM SELECT_TEST
```

# CREAR LA TABLA EJECUTANDO **SOLO EL MODELO ESPECIFICO**
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt run --models src.modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia

- models.dbt_poc.example
01:42:30  Found 3 models, 0 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 0 sources, 0 exposures, 0 metrics, 0 groups
01:42:30
01:42:31  Concurrency: 1 threads (target='dev')
01:42:31
01:42:31  1 of 1 START sql table model public.tabla_personalizada ........................ [RUN]
01:42:31  1 of 1 OK created sql table model public.tabla_personalizada ................... [SELECT 5000 in 0.18s]
01:42:31
01:42:31  Finished running 1 table model in 0 hours 0 minutes and 0.53 seconds (0.53s).
01:42:31
01:42:31  Completed successfully
01:42:31
01:42:31  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```
# Comprobar el modelo creado
<img src="imagenes\modelo_3.png">


# CREAR UNA **TABLA CON JOIN** COMO CUARTO MODELO
### dentro de la carpeta src crear un archivo sql y adicionar el codigo del ejemplo 
```
models/src/modelo_4_tabla_incremental_usando_join.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
```
## EJEMPLO TABLA INCREMENTAL, USANDO JOIN
```sql
{{
  config(
    materialized='incremental',
    incremental_strategy = 'append',
    alias='tabla_join'
    ) 
}}

WITH SELECT_JOIN AS (
    SELECT T1.* FROM {{ref('modelo_1_vista_query_directo')}} AS T1
    INNER JOIN {{ref('modelo_2_tabla_query_con_with_renombrando_columnas')}} AS T2
    ON T1.id = T2.ID
)

SELECT * FROM SELECT_JOIN
LIMIT 10
```

# CREAR LA TABLA EJECUTANDO **SOLO EL MODELO ESPECIFICO**
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt run --models src.modelo_4_tabla_incremental_usando_join

- models.dbt_poc.example
02:44:29  Found 4 models, 0 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 0 sources, 0 exposures, 0 metrics, 0 groups
02:44:29  
02:44:29  Concurrency: 1 threads (target='dev')
02:44:29  
02:44:29  1 of 1 START sql incremental model public.tabla_join ........................... [RUN]
02:44:29  1 of 1 OK created sql incremental model public.tabla_join ...................... [INSERT 0 10 in 0.23s]
02:44:29  
02:44:29  Finished running 1 incremental model in 0 hours 0 minutes and 0.48 seconds (0.48s).
02:44:29
02:44:29  Completed successfully
02:44:29
02:44:29  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```
# Comprobar el modelo creado
<img src="imagenes\modelo_4.png">

# SI SE VUELVE A EJECUTAR EL MODELO **APPEND** ADICIONA LOS REGISTROS ANTERIORES A LOS QUE YA EXISTIAN, EN OTRAS PALABRA DUPLICA LOS DATOS QUE EXISTIAN INICIALMENTE
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt run --models src.modelo_4_tabla_incremental_usando_join

- models.dbt_poc.example
02:44:29  Found 4 models, 0 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 0 sources, 0 exposures, 0 metrics, 0 groups
02:44:29  
02:44:29  Concurrency: 1 threads (target='dev')
02:44:29  
02:44:29  1 of 1 START sql incremental model public.tabla_join ........................... [RUN]
02:44:29  1 of 1 OK created sql incremental model public.tabla_join ...................... [INSERT 0 10 in 0.23s]
02:44:29  
02:44:29  Finished running 1 incremental model in 0 hours 0 minutes and 0.48 seconds (0.48s).
02:44:29
02:44:29  Completed successfully
02:44:29
02:44:29  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```
# Comprobar el modelo creado
<img src="imagenes\modelo_4.1.png">


# USAR EL ARCHIVO sources.yaml  PARA REFERENCIAS RAPIDASA LAS FUENTES DE DATOS
### dentro de la carpeta models crear un archivo yaml y adicionar el codigo del ejemplo 
```
models/sources.yaml
```

```
# SE PUEDE DEFINIR EN MODELS
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql

# SE PUEDE DEFINIR DENTRO DE SRC PARA ASOCIAR A ESOS MODELOS ESPECIFICOS
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ ⚙️ sources.yaml
```
# EJEMPLO DE sources.yaml

```yaml
version: 2

sources:

  - name: fuente_original
    database: postgres
    schema: public
    tables:
      - name: tabla_original # se puede usar como un alias en la source
        identifier: flight_logs # debe ser el nombre de la tabla en la base de datos

  - name: tabla_referencia
    database: postgres
    schema: public  
    tables:
       - name: tabla_referencia_desde_source # alias en la source
         identifier: modelo_2_tabla_query_con_with_renombrando_columnas # debe ser el nombre de la tabla en la base de datos

  - name: vista_referencia
    database: postgres
    schema: public  
    tables:
      - name: vista_referencia_desde_source # alias en la source
        identifier: modelo_1_vista_query_directo # debe ser el nombre de la tabla en la base de datos

  - name: tabla_incremental_source
    database: postgres
    schema: public  
    tables:
      - name: tabla_incremental_referencia # alias en la source
        identifier: tabla_incremental # debe ser el nombre de la tabla en la base de datos
```

# CREAR UNA **TABLA CON JOIN** COMO QUINTO MODELO
### dentro de la carpeta src crear un archivo sql y adicionar el codigo del ejemplo 
```
models/src/modelo_4_tabla_incremental_usando_join.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql    
```
## EJEMPLO TABLA USANDO SOURCE COMO REFERENCIA
```sql
{{
  config(
    materialized='view',
    alias='tabla_source'
    ) 
}}

WITH SELECT_JOIN_SOURCE_REF AS (
    SELECT T1.* FROM {{ source('fuente_original','tabla_original') }} AS T1
    LEFT JOIN {{ ref('modelo_2_tabla_query_con_with_renombrando_columnas') }} AS T2
    ON T1.id = T2.ID
)

SELECT * 
FROM SELECT_JOIN_SOURCE_REF
WHERE id = 1
```

# CREAR LA TABLA EJECUTANDO **SOLO EL MODELO ESPECIFICO**
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt run --models src.modelo_5_tabla_usando_el_alias_del_source

- models.dbt_poc.example
03:41:36  Found 5 models, 0 tests, 0 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
03:41:36
03:41:36  Concurrency: 1 threads (target='dev')
03:41:36
03:41:36  1 of 1 START sql view model public.tabla_source ................................ [RUN]
03:41:36  1 of 1 OK created sql view model public.tabla_source ........................... [CREATE VIEW in 0.15s]
03:41:37
03:41:37  Finished running 1 view model in 0 hours 0 minutes and 0.50 seconds (0.50s).
03:41:37
03:41:37  Completed successfully
03:41:37
03:41:37  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```
# Comprobar el modelo creado
<img src="imagenes\modelo_5.png">


# FRESHNESS
Imagina que tienes una caja llena de diferentes juguetes. Cada juguete tiene una etiqueta que muestra cuándo fue la última vez que lo usaste. Esa etiqueta es como el "freshness" en dbt.

El "freshness" en dbt se refiere a la actualidad de los datos en una base de datos. Piensa en una base de datos como una enorme colección de información almacenada en un ordenador. Los datos pueden provenir de muchas fuentes diferentes, como ventas de una tienda, registros de estudiantes en una escuela o información meteorológica.

Para asegurarnos de que los datos en la base de datos estén actualizados, necesitamos verificar su "freshness". Esto significa que debemos comprobar cuándo fue la última vez que se actualizaron esos datos. Es como mirar las etiquetas de los juguetes en la caja para saber cuándo los usaste por última vez.

Cuando trabajamos con bases de datos y dbt, es importante que los datos sean "fresh" o actualizados. Esto nos ayuda a tomar decisiones basadas en información reciente. Por ejemplo, si queremos saber cuántas camisetas se vendieron en una tienda hoy, necesitamos datos frescos para obtener una respuesta precisa.

En resumen, el "freshness" en dbt se refiere a la actualidad de los datos en una base de datos, como la etiqueta en un juguete que muestra cuándo fue la última vez que se usó. Es importante tener datos actualizados para tomar decisiones informadas.

## SE TRATA DE VALIDAR QUE LA TABLA DONDE ALMACENAMOS LOS DATOS, SE ESTE ACTUALIZANDO PERIODICAMENTE EN EL TIEMPO DETERMINADO, SINO MUESTRA UN **WARNING** O **ERROR** SEGUN EL CASO

| FRESHNESS VALUES|
|-----------------|
| minute |
| hour |
| day|

# ADICIONA UNA COLUMNA TIMESTAMP PARA HACER LA PRUEBA
```sql
ALTER TABLE public.flight_logs 
ADD COLUMN test_time_freshness TIMESTAMP NULL DEFAULT now();
```

<img src="imagenes\freshness_adicionar_columna.png">


# ACTUALIZAMOS el sources.yaml
# **ATENCION A LA HORA DE DBT** Y LA **HORA DE INSERCION A LA BASE DE DATOS**, PUEDE TENER UNA GRAN DIFERENCIA Y HACE QUE LA PRUEBA FALLE INMEDIATAMENTE

```yaml
version: 2

sources:

  - name: fuente_original
    description: Fuente de datos original creada con el csv
    
    database: postgres
    schema: public

    freshness: # si se ubica antes de las tablas aplica para todas las tablas
      warn_after:
        count: 1
        period: day # si en este tiempo 1 minuto no hay nuevos registros y actualizada la columna de timestamp 'test_time_freshness' muestra la alerta
      error_after:
        count: 3
        period: day  # si en este tiempo 3 minutos no hay nuevos registros y actualizada la columna de timestamp 'test_time_freshness' muestra el error      

    tables:
      - name: tabla_original # se puede usar como un alias en la source
        identifier: flight_logs # debe ser el nombrede la tabla en la base de datos
        # cmapo que sirve para probar que tan a menudo se actualiza la tabla 
        loaded_at_field: test_time_freshness # tiene que ser un campo TIMESTAMP de la tabla para el freshness 

  - name: tabla_referencia
    database: postgres
    schema: public  
    tables:
       - name: tabla_referencia_desde_source # alias en la source
         identifier: modelo_2_tabla_query_con_with_renombrando_columnas # debe ser el nombre de la tabla en la base de datos

  - name: vista_referencia
    database: postgres
    schema: public  
    tables:
      - name: vista_referencia_desde_source # alias en la source
        identifier: modelo_1_vista_query_directo # debe ser el nombre de la tabla en la base de datos

  - name: tabla_incremental_source
    database: postgres
    schema: public  
    tables:
      - name: tabla_incremental_referencia # alias en la source
        identifier: tabla_incremental # debe ser el nombre de la tabla en la base de datos
```

# VALIDANDO SIN QUE PASE EL INTERVALO INICIAL DE 1 MINUTO
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt source freshness

05:16:01  Found 4 models, 0 tests, 2 snapshots, 0 analyses, 172 macros, 0 operations, 2 seed files, 3 sources, 0 exposures, 0 metrics
05:16:01
05:16:01  Concurrency: 1 threads (target='dev')
05:16:01
05:16:01  1 of 1 START freshness of fuente_original.tabla_original ....................... [RUN]
05:16:01  1 of 1 PASS freshness of fuente_original.tabla_original ........................ [PASS in 0.04s]
```

# VALIDANDO WARNINGS, YA PASO 1 MINUTO Y EJECUTANDO SOLO PARA ESA FUENTE
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt source freshness --select source:fuente_original

05:04:57  Found 4 models, 0 tests, 2 snapshots, 0 analyses, 172 macros, 0 operations, 2 seed files, 3 sources, 0 exposures, 0 metrics
05:04:57
05:04:57  Concurrency: 1 threads (target='dev')
05:04:57  
05:04:57  1 of 1 START freshness of fuente_original.tabla_original ....................... [RUN]
05:04:57  1 of 1 WARN freshness of fuente_original.tabla_original ........................ [WARN in 0.04s]
05:04:57  Done.
```

# VALIDANDO ERRORES, YA PASARON 2 MINUTOS
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt source freshness --select source:fuente_original

05:04:40  Concurrency: 1 threads (target='dev')
05:04:40
05:04:40  1 of 1 START freshness of fuente_original.tabla_original ....................... [RUN]
05:04:40  1 of 1 ERROR STALE freshness of fuente_original.tabla_original ................. [ERROR STALE in 0.04s]
05:04:40
```

# INSERTANDO NUEVOS DATOS
```sql
INSERT INTO public.flight_logs
VALUES ('7777', '01H4EEMMVWTD0QNCNHCWDQ7Y40', '2014', '2309', 'United', 'RST', 'Gabriela Zea', 'Colombia', '2022-03-30', '2023-07-07 14:14:22', 'CRY', 'Kaseda-shirakame', 'Japan', '26-1-2022', '2023-07-06 00:46:28', '5.55', 'Rici Preon', '8', 'Female', 'China', 'C3', '501.04', 'DOP', '43.15', 'B2', 'F6', 'Departed', 'Carolee Bonett', 'Adriena Burbury', '7', 'Boeing 737', 'N12345', '2884.71', '3647.15', now());
```
# VALIDANDO SIN QUE PASE EL INTERVALO INICIAL DE 1 MINUTO
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt source freshness --select source:fuente_original

05:16:01  Found 4 models, 0 tests, 2 snapshots, 0 analyses, 172 macros, 0 operations, 2 seed files, 3 sources, 0 exposures, 0 metrics
05:16:01
05:16:01  Concurrency: 1 threads (target='dev')
05:16:01
05:16:01  1 of 1 START freshness of fuente_original.tabla_original ....................... [RUN]
05:16:01  1 of 1 PASS freshness of fuente_original.tabla_original ........................ [PASS in 0.04s]
```


# SNAPSHOT

Imagina que tienes una cámara que toma fotos de tus juguetes y las imprime en papel. Cada foto es como un "snapshot" en dbt.

En dbt, un "snapshot" es una imagen o una captura de los datos en un momento específico. Es como tomar una foto de los datos en un momento determinado y guardarla para poder verla más adelante.

Cuando trabajamos con bases de datos, los datos pueden cambiar con el tiempo. Es como si tus juguetes se movieran o cambiaran de forma. Pero a veces queremos guardar una imagen fija de esos datos en un punto específico.

Por ejemplo, imagina que tienes una lista de tus juguetes favoritos en una hoja de papel. Si tomas una foto de esa lista y la guardas, tendrás un "snapshot" de tus juguetes favoritos en ese momento. Incluso si más tarde añades o quitas juguetes de la lista, siempre podrás volver a esa foto y recordar cómo era tu lista original.

En dbt, los "snapshots" se utilizan para guardar copias de seguridad de los datos en un momento específico. Esto nos permite conservar una imagen de los datos tal como eran en ese momento, aunque puedan cambiar más adelante.

En resumen, los "snapshots" en dbt son como tomar una foto de los datos en un momento específico y guardarla para poder verla más adelante. Es útil para conservar una imagen fija de los datos, incluso si cambian con el tiempo. Es como tener una foto de tus juguetes favoritos para recordar cómo eran en ese momento.

# CREAR EL PRIMER SNAPSHOT
### dentro de la carpeta snapshots crear un archivo sql y adicionar el codigo del ejemplo 
```
snapshots/snapshot_1_tabla_validar_multi_campos_snapshot.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql        
```

```sql
-- en MySQL si ponemos una database que no existe la crea
-- en Postgres tiene que existir la base de datos
-- target_database='dbt_snapshots'
-- target_schema='dbt_snapshots'
{% snapshot validar_multi_campos_snapshot %}

{{
  config(
    target_database='postgres',
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

# EJECUTAR EL SNAPSHOT

```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt snapshot

- models.dbt_poc.example
22:22:38  Found 5 models, 0 tests, 1 snapshot, 0 analyses, 307 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
22:22:38  
22:22:38  Concurrency: 1 threads (target='dev')
22:22:38  
22:22:38  1 of 1 START snapshot dbt_snapshots.validar_multi_campos_snapshot .............. [RUN]
22:22:38  1 of 1 OK snapshotted dbt_snapshots.validar_multi_campos_snapshot .............. [success in 0.27s]
22:22:38  
22:22:38  Finished running 1 snapshot in 0 hours 0 minutes and 0.78 seconds (0.78s).
22:22:38
22:22:38  Completed successfully
```

# Comprobar el snapshot creado
<img src="imagenes\snapshot_1.png">


# CREAR EL SEGUNDO SNAPSHOT
### dentro de la carpeta snapshots crear un archivo sql y adicionar el codigo del ejemplo 
```
snapshots/snapshot_2_tabla_validar_todos_los_campos.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql 
```
     
```sql
{% snapshot validar_todos_los_campos_snapshot %}

{{
  config(
    target_database='postgres',
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

# EJECUTAR EL SNAPSHOT DE ESTE CASO
```
(venv) jorge@cardona/dbt_poc:~$ dbt snapshot --select snapshot_2_tabla_validar_todos_los_campos

- models.dbt_poc.example
22:36:26  Found 5 models, 0 tests, 2 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
22:36:26
22:36:26  Concurrency: 1 threads (target='dev')
22:36:26
22:36:26  1 of 1 START snapshot dbt_snapshots_todos_los_campos.validar_todos_los_campos_snapshot  [RUN]
22:36:27  1 of 1 OK snapshotted dbt_snapshots_todos_los_campos.validar_todos_los_campos_snapshot  [success in 0.17s]
22:36:27
22:36:27  Finished running 1 snapshot in 0 hours 0 minutes and 0.56 seconds (0.56s).
22:36:27
22:36:27  Completed successfully
```

# Comprobar el snapshot creado
<img src="imagenes\snapshot_2.png">

# MODIFICAR UN REGISTRO CON 1 CAMPO CUALQUIERA

```sql
UPDATE postgres.public.flight_logs 
SET secure_code = 1
WHERE id = 1;
```
<img src="imagenes\snapshot_actualizacion_1.png">

# EJECUTAR EL SNAPSHOT PARA VER SI AFECTARON LOS CAMBIOS DE LA TABLA DONDE SE COPIARON LOS DATOS
```
(venv) jorge@cardona/dbt_poc:~$ dbt snapshot
```
# SE AFECTA EL QUE VALIDA TODOS LOS CAMPOS, PORQUE secure_code NO ESTA DECLARADO COMO VALIDACION EN LA OTRA SNAPSHOT
# SE ADICIONO UN NUEVO REGISTRO CON LOS CAMBIOS ACTUALES
<img src="imagenes\snapshot_comparacion_1.png">


# MODIFICAR EL REGISTRO DE NUEVO CON UN CAMPO RELACIONADO EN LA RESTRICCION

```sql
UPDATE postgres.public.flight_logs 
SET secure_code = 1
WHERE id = 1;
```

<img src="imagenes\snapshot_actualizacion_2.png">

# EJECUTAR EL SNAPSHOT
```
(venv) jorge@cardona/multi_database:~$ dbt snapshot
```

# SE AFECTA AMBAS TABLAS POR QUE TIENEN UN CAMPO EN COMUN MODIFICADO
<img src="imagenes\snapshot_comparacion_2.png">
 

# TEST

Imagina que tienes una lista de tareas para hacer y quieres asegurarte de que las completes correctamente. Los "tests" en dbt son como las pruebas que haces para verificar si has realizado esas tareas correctamente.

En dbt, los "tests" se utilizan para verificar si los datos en una base de datos cumplen ciertos criterios o reglas. Es como tener una lista de verificación para asegurarse de que los datos estén correctos y no tengan errores.

Piensa en un juego en el que debes organizar diferentes juguetes en cajas según su color. Si tienes una caja para los juguetes rojos, una para los juguetes azules y otra para los juguetes verdes, puedes hacer un "test" para comprobar si cada juguete está en la caja correcta.

Los "tests" en dbt funcionan de manera similar. Puedes crear reglas o criterios que los datos deben cumplir, como "el campo 'edad' debe ser un número entero" o "el campo 'nombre' no debe estar vacío". Luego, dbt realizará esos "tests" en los datos y te dirá si cumplen con esas reglas o si hay algún error.

Los "tests" son importantes porque ayudan a garantizar la calidad de los datos. Al igual que tú quieres asegurarte de que los juguetes estén en las cajas correctas, los "tests" en dbt nos ayudan a asegurarnos de que los datos estén limpios y precisos.

En resumen, los "tests" en dbt son como pruebas o reglas que se utilizan para verificar si los datos cumplen con ciertos criterios. Son como una lista de verificación para asegurarse de que los datos estén correctos y sin errores. Es como organizar los juguetes en las cajas correctas según su color.

# LOS RESULTADOS DE LOS TEST **SIEMPRE DEBE SER 0 COLUMNAS CONTADAS** PARA QUE EL TEST PASE, DE LO CONTRARIO MOSTRARA ERROR

| TEST TYPES|
|-----------|

| Singular        | Generic   |
|-----------------|-----------|
| Unique          | custome |
| not_null        |       |
| accepted_values |      |
| Relationships   |   |


# GENERIC TEST DESDE EL YAML schema.yaml
### dentro de la carpeta models y el archivo schema. yaml y adicionar el codigo del ejemplo 
```
models/schema.yaml
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ⚜️ schema.yaml
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql      
```

# EJEMPLO DE CODIGO DEL YAML
```yaml
version: 2

models:
  - name: flight_logs # se puede usar el nombre del script sql o el identifier
    columns:
      - name: id
        tests:
          - unique 
      - name: departure_gate
        tests:
          - not_null
          - accepted_values:
              name: valores_esperados # nombre del caso de prueba
              values: ['A1', 'B2', 'C3'] 
              config:
                where: "id > 1"
```
# EJECUTAR LAS PRUEBAS DE VALIDACION DE DATOS DEL MODELO
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt test

03:31:25  1 of 3 START test not_null_flight_logs_departure_gate .......................... [RUN]
03:31:25  1 of 3 PASS not_null_flight_logs_departure_gate ................................ [PASS in 0.05s]
03:31:25  2 of 3 START test unique_flight_logs_id ........................................ [RUN]
03:31:25  2 of 3 PASS unique_flight_logs_id .............................................. [PASS in 0.03s]
03:31:25  3 of 3 START test valores_esperados ............................................ [RUN]
03:31:26  3 of 3 PASS valores_esperados .................................................. [PASS in 0.04s]
03:31:26  
03:31:26  Finished running 3 tests in 0.25s.
03:31:26  Completed successfully
03:31:26  Done. PASS=3 WARN=0 ERROR=0 SKIP=0 TOTAL=3
```

# VALIDACIONES FALLIDAS, ACTUALIZAR EL schema.yaml
```yaml
version: 2

models:
  - name: flight_logs # se puede usar el nombre del script sql o el identifier
    columns:
      - name: id
        tests:
          - unique 
      - name: departure_gate
        tests:
          - not_null
          - accepted_values:
              name: valores_esperados # nombre del caso de prueba
              values: ['A1', 'B2'] 
              config:
                where: "id > 1"
```
# EJECUTAR LAS PRUEBAS DE VALIDACION DE DATOS EL TEST FALLA POR QUE EL VALOR C3 NO ESTA COMO VALOR ESPERADO
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt test

03:33:14  1 of 3 START test not_null_flight_logs_departure_gate .......................... [RUN]
03:33:15  1 of 3 PASS not_null_flight_logs_departure_gate ................................ [PASS in 0.05s]
03:33:15  2 of 3 START test unique_flight_logs_id ........................................ [RUN]
03:33:15  2 of 3 PASS unique_flight_logs_id .............................................. [PASS in 0.04s]
03:33:15  3 of 3 START test valores_esperados ............................................ [RUN]
03:33:15  3 of 3 FAIL 1 valores_esperados ................................................ [FAIL 1 in 0.03s]
03:33:15  
03:33:15  Finished running 3 tests in 0.26s.
03:33:15  Completed with 1 error and 0 warnings:
03:33:15  Failure in test valores_esperados (models\schema.yaml)
03:33:15    Got 1 result, configured to fail if != 0
03:33:15    compiled SQL at target\compiled\dbt_mysql_poc\models\schema.yaml\valores_esperados.sql
```

# SE PUEDE ACCEDER AL CASO DE PRUEBA CREADO Y VER EL CODIGO GENERADO POR DBT Y VEMOS QUE HAY MAS DE 1 ARCHIVO, POR ESO GENERA ERROR YA QUE DEBERIA SER 0
``` SQL
-- compiled SQL at target\compiled\dbt_mysql_poc\models\schema.yaml\valores_esperados.sql

with all_values as (

    select
        departure_gate as value_field,
        count(*) as n_records

    from (select * from `test_poc`.`flight_logs` where id > 1) dbt_subquery
    group by departure_gate

)

select *
from all_values
where value_field not in (
    'A1','B2'
)
```

# TEST SINGULAR O TEST PERSONALIZADOS CON SQL
### dentro de la carpeta test crear un archivo .sql  y adicionar el codigo del ejemplo 
```
test/validar_menores_de_edad.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ⚜️ schema.yaml
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql
  ┗ 🚀 test [package]
    ┗ test_1_verificar_que_no_hay_menores_de_edad.sql    
```

# EJEMPLO DE CODIGO DEL TEST, CON EXCEPCION PERSONALIZADA
# LANZA LA EXCEPCION SI EXISTEN MENORES DE EDAD EN EL VUELO
```sql
SELECT CASE
    WHEN (
            SELECT COUNT(passenger_age) FROM 
                    {{ ref('flight_logs') }}
            WHERE passenger_age < 18
          ) > 0 THEN 
                    NULL
    ELSE
        RAISE EXCEPTION 'HAY MENORES DE EDAD EN EL VUELO'
END
```

# EJECUTAR LAS PRUEBAS DE VALIDACION DE DATOS DEL CASO ESPECIFICO FALLA POR QUE HAY MENORES DE EDAD
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt test --select test_1_verificar_que_no_hay_menores_de_edad

- models.dbt_poc.example
04:12:33  Found 5 models, 4 tests, 2 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
04:12:33
04:12:33  Concurrency: 1 threads (target='dev')
04:12:33  
04:12:33  1 of 1 START test test_1_verificar_que_no_hay_menores_de_edad ...................................... [RUN]
04:12:33  1 of 1 FAIL 5 test_1_verificar_que_no_hay_menores_de_edad .......................................... [FAIL 5 in 0.09s]
04:12:34  
04:12:34  Finished running 1 test in 0 hours 0 minutes and 0.54 seconds (0.54s).
04:12:34
04:12:34  Completed with 1 error and 0 warnings:
04:12:34  
04:12:34  Failure in test test_1_verificar_que_no_hay_menores_de_edad (tests\test_1_verificar_que_no_hay_menores_de_edad.sql)
04:12:34    Got 5 results, configured to fail if != 0
04:12:34
04:12:34    compiled Code at target\compiled\dbt_poc\tests\test_1_verificar_que_no_hay_menores_de_edad.sql
```

### dentro de la carpeta test crear un archivo .sql  y adicionar el codigo del ejemplo 
```
test/test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ⚜️ schema.yaml
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql
  ┗ 🚀 test [package]
    ┗ test_1_verificar_que_no_hay_menores_de_edad.sql
    ┗ test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql    
```

# EJEMPLO DE CODIGO DEL TEST 2
```sql
SELECT CASE
    WHEN (
            SELECT COUNT(*) 
                FROM {{ ref('flight_logs') }}
            WHERE 'XANADU' IN (departure_city, arrival_city)
          ) > 0 THEN 
                    NULL
    ELSE
        RAISE EXCEPTION 'NO EXISTEN VUELOS DE O HACIA XANADU'
END
```

# EJECUTAR LAS PRUEBAS DE VALIDACION DE DATOS DEL CASO ESPECIFICO FALLA POR QUE HAY MENORES DE EDAD
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt test --select test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu

- models.dbt_poc.example
04:47:14  Found 5 models, 5 tests, 2 snapshots, 0 analyses, 307 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
04:47:14  
04:47:15  Concurrency: 1 threads (target='dev')
04:47:15  
04:47:15  1 of 1 START test test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu ....... [RUN]
04:47:15  1 of 1 ERROR test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu ............ [ERROR in 0.09s]
04:47:15  
04:47:15  Finished running 1 test in 0 hours 0 minutes and 0.56 seconds (0.56s).
04:47:15  
04:47:15  Completed with 1 error and 0 warnings:
04:47:15
04:47:15  Database Error in test test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu (tests\test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql)
04:47:15    error de sintaxis en o cerca de «EXCEPTION»
04:47:15    LINE 15:         RAISE EXCEPTION 'NO EXISTEN VUELOS DE O HACIA XANADU...
04:47:15                           ^
04:47:15    compiled Code at target\run\dbt_poc\tests\test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql
04:47:15
04:47:15  Done. PASS=0 WARN=0 ERROR=1 SKIP=0 TOTAL=1
```

# MACROS

Imagina que estás construyendo una casa de juguete y necesitas hacer varias piezas iguales. En lugar de construir cada pieza desde cero una y otra vez, puedes usar una máquina especial que hace copias exactas de la pieza. Esa máquina es como un "macro" en dbt.

En dbt, un macro es como una máquina que guarda un conjunto de instrucciones o código que puedes reutilizar en diferentes partes de tu proyecto de análisis de datos. Es como una forma de automatizar una tarea que tienes que hacer repetidamente.

Por ejemplo, supongamos que en tu análisis de datos siempre necesitas calcular la suma de una columna en una tabla. En lugar de escribir la misma fórmula una y otra vez, puedes crear un macro que haga ese cálculo por ti. Luego, cada vez que necesites calcular la suma, simplemente llamas al macro y él se encargará de hacer el cálculo automáticamente.

Los macros en dbt pueden ser útiles porque te ahorran tiempo y esfuerzo al automatizar tareas repetitivas. Puedes crear tus propios macros personalizados para adaptarse a tus necesidades específicas en el análisis de datos.

En resumen, un macro en dbt es como una máquina especial que guarda un conjunto de instrucciones o código que puedes reutilizar en diferentes partes de tu análisis de datos. Es como una forma de automatizar tareas repetitivas y ahorrar tiempo y esfuerzo. Es como usar una máquina para hacer copias exactas de una pieza de una casa de juguete en lugar de construir cada una desde cero.

### dentro de la carpeta macro crear un archivo .sql  y adicionar el codigo del ejemplo 
```
macro/macro_sin_valores_nulos.sql
```
# EJEMPLO DE CODIGO SQL PARA MACRO
```sql
{% macro check_null_values(model) %}
    SELECT * FROM {{ model }} WHERE
    {% for col in adapter.get_columns_in_relation(model) -%} 
        {{ col.column }} IS NULL OR
    {% endfor %}
        FALSE
{% endmacro %}
```
### dentro de la carpeta macro test un archivo .sql  y adicionar el codigo del ejemplo 
```
test/test_3_check_null_values_desde_el_macro.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ⚜️ schema.yaml
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql
  ┗ 🚀 test [package]
    ┗ test_1_verificar_que_no_hay_menores_de_edad.sql
    ┗ test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql
    ┗ test_3_check_null_values_desde_el_macro.sql
  ┗ 🦄 macros
    ┗ macro_sin_valores_nulos.sql
```

# EJEMPLO DE CODIGO SQL PARA TEST USANDO LA MACRO
```sql
{{ check_null_values (ref('flight_logs')) }}
```
# EJECUTAR EL TEST
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt test --select test_3_check_null_values_desde_el_macro

- models.dbt_poc.example
04:58:14  Found 5 models, 6 tests, 2 snapshots, 0 analyses, 308 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
04:58:14
04:58:14  Concurrency: 1 threads (target='dev')
04:58:14  
04:58:14  1 of 1 START test test_3_check_null_values_desde_el_macro ...................... [RUN]
04:58:14  1 of 1 PASS test_3_check_null_values_desde_el_macro ............................ [PASS in 0.10s]
04:58:14  
04:58:14  Finished running 1 test in 0 hours 0 minutes and 0.58 seconds (0.58s).
04:58:14  
04:58:14  Completed successfully
```

# EJECUTAR ESTE SQL PARA CREAR REGISTRO CON VALORES NULOS
```sql
INSERT INTO postgres.public.flight_logs (id) VALUES ('12345678');
```

# VALIDAR EL REGISTRO INSERTADO
<img src="imagenes\test_1_usando_macros.png">


# VOLVER A EJECUTAR EL TEST
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt test --select check_null_values_desde_el_macro

- models.dbt_poc.example
05:03:22  Found 5 models, 6 tests, 2 snapshots, 0 analyses, 308 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
05:03:22  
05:03:23  Concurrency: 1 threads (target='dev')
05:03:23  
05:03:23  1 of 1 START test test_3_check_null_values_desde_el_macro ...................... [RUN]
05:03:23  1 of 1 FAIL 1 test_3_check_null_values_desde_el_macro .......................... [FAIL 1 in 0.10s]
05:03:23  
05:03:23  Finished running 1 test in 0 hours 0 minutes and 0.40 seconds (0.40s).
05:03:23
05:03:23  Completed with 1 error and 0 warnings:
05:03:23
05:03:23  Failure in test test_3_check_null_values_desde_el_macro (tests\test_3_check_null_values_desde_el_macro.sql)
05:03:23    Got 1 result, configured to fail if != 0
05:03:23
05:03:23    compiled Code at target\compiled\dbt_poc\tests\test_3_check_null_values_desde_el_macro.sql
```
# ADICIONAR UN NUEVO MACRO
### dentro de la carpeta macro test un archivo .sql  y adicionar el codigo del ejemplo 
```
macro/macro_validar_adultos_mayores.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ⚜️ schema.yaml
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql
  ┗ 🚀 test [package]
    ┗ test_1_verificar_que_no_hay_menores_de_edad.sql
    ┗ test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql
    ┗ test_3_check_null_values_desde_el_macro.sql
  ┗ 🦄 macros
    ┗ macro_sin_valores_nulos.sql
    ┗ macro_validar_adultos_mayores.sql
```

# CODIGO DE EJEMPLO DEL MACRO
```sql
{% test tercera_edad(model, column_name) %}
SELECT
 *
FROM
 {{ model }}
WHERE
 {{ column_name }} > 80
{% endtest %}
```

# ACTUALIZAR EL schema.yml
```yaml
version: 2

models:
  - name: flight_logs # se puede usar el nombre del script sql o el identifier
    columns:
      - name: id
        tests:
          - unique 
      - name: departure_gate
        tests:
          - not_null
          - accepted_values:
              name: valores_esperados # nombre del caso de prueba
              values: ['A1', 'B2', 'C3'] # ['A1', 'B2', 'C3']
              config:
                where: "id > 1"
      - name: passenger_age
        tests: 
          - tercera_edad
```

# EJECUTAR EL TEST
```yaml
(venv) jorge@cardona/dbt_poc:~$  dbt test --select tercera_edad_flight_logs_passenger_age

- models.dbt_poc.example                                                                                        
05:08:55  Found 5 models, 7 tests, 2 snapshots, 0 analyses, 309 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
05:08:55  
05:08:56  Concurrency: 1 threads (target='dev')
05:08:56  
05:08:56  1 of 1 START test tercera_edad_flight_logs_passenger_age ....................... [RUN]
05:08:56  1 of 1 FAIL 1208 tercera_edad_flight_logs_passenger_age ........................ [FAIL 1208 in 0.09s]
05:08:56  
05:08:56  Finished running 1 test in 0 hours 0 minutes and 0.39 seconds (0.39s).
05:08:56  
05:08:56  Completed with 1 error and 0 warnings:
05:08:56
05:08:56  Failure in test tercera_edad_flight_logs_passenger_age (models\schema.yaml)
05:08:56    Got 1208 results, configured to fail if != 0
05:08:56
05:08:56    compiled Code at target\compiled\dbt_poc\models\schema.yaml\tercera_edad_flight_logs_passenger_age.sql
05:08:56
05:08:56  Done. PASS=0 WARN=0 ERROR=1 SKIP=0 TOTAL=1
```

# DEFINIENDO VARIABLES LOCALES CON SET Y USARLAS
# USANDO EL LOG PARA VER EL CONTENIDO DE LAS VARIABLES

# ADICIONAR UN NUEVO MODELO
### dentro de la carpeta models/src test un archivo .sql  y adicionar el codigo del ejemplo 
```
models/src/modelo_6_set_1_con_jinja.sql
```


```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ⚜️ schema.yaml
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
    ┗ modelo_6_set_1_con_jinja.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql
  ┗ 🚀 test [package]
    ┗ test_1_verificar_que_no_hay_menores_de_edad.sql
    ┗ test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql
    ┗ test_3_check_null_values_desde_el_macro.sql
  ┗ 🦄 macros
    ┗ macro_sin_valores_nulos.sql
    ┗ macro_validar_adultos_mayores.sql
```

# EJEMPLO DEL MODELO
```sql
{{
  config(
    materialized='view',
    alias='jinja_test_set'
  )
}}


{% set seat_numbers = ('A1', 'B2', 'C3') %}

-- VER EL LOG SIN LA FECHA a la izquierda en la salida estándar
{% do log(print("--- El valor de seat_numbers es: " ~ seat_numbers), info=True) %}
-- Imprimir el valor de seat_numbers en la salida estándar
{% do log("*** El valor de seat_numbers es: " ~ seat_numbers, info=True) %}

WITH result_table AS (
  SELECT *
    FROM  {{ref('flight_logs')}}
  WHERE seat_number IN {{ seat_numbers }}
    LIMIT 10
)

SELECT *
FROM result_table
```
# EJECUTAR EL MODELO
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt run --models dbt run --models modelo_6_set_1_con_jinja

- models.dbt_poc.example
05:19:59  Found 6 models, 7 tests, 2 snapshots, 0 analyses, 310 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
05:19:59  
05:19:59  Concurrency: 1 threads (target='dev')
05:19:59  
05:19:59  1 of 1 START sql view model public.jinja_test_set .............................. [RUN]
--- El valor de seat_numbers es: ('A1', 'B2', 'C3')
05:19:59
05:19:59  *** El valor de seat_numbers es: ('A1', 'B2', 'C3')
05:20:00  1 of 1 OK created sql view model public.jinja_test_set ......................... [CREATE VIEW in 0.29s]
05:20:00  
05:20:00  Finished running 1 view model in 0 hours 0 minutes and 0.81 seconds (0.81s).
05:20:00
05:20:00  Completed successfully
```

# USAR MACROS DENTRO DE MODELOS
# ADICIONAR UN NUEVO MACRO
### dentro de la carpeta macro un archivo .sql  y adicionar el codigo del ejemplo 
```
macro/macro_filro_con_set.sql
```
# DEFINIR EL MACRO, poner siempre el -% ya que genera lineas o espacios en blanco y entregando una respuesta mal
# EJEMPLO DE MACRO
```sql
{%- macro  filtrar_valores_usando_un_macro(query) -%}
    {%- set filtrar -%}
        {{query}}
    {%- endset -%}

    {% do log(print("--- El query a ejecutar es: " ~ filtrar), info=True) %}
    {%- set resultado_query = run_query(filtrar) -%}

    {%- if execute -%}
        {# Return the first column #}
        {% set results_list = resultado_query.columns[0].values() %}
    {%- else -%}
        {% set results_list = [] %}
    {%- endif -%}
    
{% do log(print("--- El valor de results_list del query es: " ~ results_list), info=True) %}

{{results_list}} {# esto hace las veces de retorno de variables {{nombre_de_la_variable_a_retornar}}, sino queda como retorno vacio #}
{% endmacro %}
```


```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ⚜️ schema.yaml
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
    ┗ modelo_6_set_1_con_jinja.sql
    ┗ modelo_7_usar_macro.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql
  ┗ 🚀 test [package]
    ┗ test_1_verificar_que_no_hay_menores_de_edad.sql
    ┗ test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql
    ┗ test_3_check_null_values_desde_el_macro.sql
  ┗ 🦄 macros
    ┗ macro_sin_valores_nulos.sql
    ┗ macro_validar_adultos_mayores.sql
    ┗ macro_filro_con_set.sql
```

# EJEMPLO DE MODELO
# ADICIONAR UN NUEVO MODELO
### dentro de la carpeta models/src test un archivo .sql  y adicionar el codigo del ejemplo 
```
models/modelo_7_usar_macro.sql
```
```sql
{% set query_generos_registrados %}
  SELECT DISTINCT passenger_gender
    FROM  {{ref('flight_logs')}}
    WHERE passenger_gender IS NOT NULL -- evita que retorne valores nulos
{% endset %}

{%- set results_list -%}
    {# AQUI SE LLAMA LA FUNCION CREADA EN EL MACRO Y SE LE PASAN LOS PARAMETROS DE LA FUNCION #}
    {{ filtrar_valores_usando_un_macro(query_generos_registrados)}}
{%- endset -%}

-- VER EL LOG SIN LA FECHA a la izquierda en la salida estándar
{% do log(print("--- El valor de results_list en usar_macro es : " ~ results_list), info=True) %}

-- hacer el query con los valores filtrados
WITH result_table AS (
  SELECT *
    FROM  {{ref('flight_logs')}}
  WHERE passenger_gender IN {{ results_list}}
    LIMIT 10
)

SELECT *
FROM result_table
```

# EJECUTAR EL MODELO
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt run --models modelo_7_usar_macro

05:24:18  Found 7 models, 7 tests, 2 snapshots, 0 analyses, 310 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
05:24:18  
05:24:18  Concurrency: 1 threads (target='dev')
05:24:18  
05:24:18  1 of 1 START sql view model public.modelo_7_usar_macro ......................... [RUN]
--- El query a ejecutar es: 
  SELECT DISTINCT passenger_gender
    FROM  "postgres"."public"."flight_logs"
    WHERE passenger_gender IS NOT NULL -- evita que retorne valores nulos

05:24:18
--- El valor de results_list del query es: ('Genderqueer', 'Bigender', 'Genderfluid', 'Male', 'Non-binary', 'Polygender', 'Female', 'Agender')
05:24:18  
--- El valor de results_list en usar_macro es :

('Genderqueer', 'Bigender', 'Genderfluid', 'Male', 'Non-binary', 'Polygender', 'Female', 'Agender')

05:24:18
05:24:18  1 of 1 OK created sql view model public.modelo_7_usar_macro .................... [CREATE VIEW in 0.18s]
05:24:18  
05:24:18  Finished running 1 view model in 0 hours 0 minutes and 0.52 seconds (0.52s).
05:24:18  
05:24:18  Completed successfully
05:24:18
05:24:18  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```

# USANDO VARIABLES DE PROYECTO

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ⚜️ schema.yaml
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
    ┗ modelo_6_set_1_con_jinja.sql
    ┗ modelo_7_usar_macro.sql
    ┗ modelo_8_usando_variables_dbt_project.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql
  ┗ 🚀 test [package]
    ┗ test_1_verificar_que_no_hay_menores_de_edad.sql
    ┗ test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql
    ┗ test_3_check_null_values_desde_el_macro.sql
  ┗ 🦄 macros
    ┗ macro_sin_valores_nulos.sql
    ┗ macro_validar_adultos_mayores.sql
    ┗ macro_filro_con_set.sql
  ┗ 🔑 dbt_project.yml
```
# EDITAR EL ARCHIVO dbt_project.yml ADICIONANDO LA SECCION var
# YAML BASE

```yaml
...
...
...
models:
  dbt_poc:
    # Config indicated by + and applies to all files under models/example/
    example:
      +materialized: view
```
# ADICIONAR ESTE CODIGO AL FINAL

```yaml
# variables personalizadas
# SE PUEDEN DECLARAN LOS VALORES DE CADENA SIN COMILLAS
vars:
  tipo_de_avion : Embraer E190
  maximos_registros: 3

# SE RECOMIENDA DECLARA LOS VALORES DE CADENA CON COMILLAS, PARA EVITAR ESPACIOS EN BLANCO, ETC
vars:
  tipo_de_avion : 'Embraer E190'
  maximos_registros: 3
```
# YAML FINAL
#
```yaml
...
...
...
models:
  dbt_poc:
    # Config indicated by + and applies to all files under models/example/
    example:
      +materialized: view

# variables personalizadas
# variables personalizadas
vars:
  tipo_de_avion : 'Embraer E190'
  maximos_registros: 3
```
# ADICIONAR UN NUEVO MODELO
### dentro de la carpeta models/scr adicionar un archivo .sql  y adicionar el codigo del ejemplo 

```yaml
models/src/modelo_8_usando_variables_dbt_project.sql
```

# CODIGO DE EJMEPLO USANDO LA VARIABLE var
#
```sql
{{ 
config(
		materialized='view', 
		alias='vista_usando_variables'
		) 
}}

-- MANEJO ESPECIAL CON COMILLAS DOBLES AL TRAER LOS VALORES DE LAS var, DADO QUE AL COMPARAR EN EL WHERE DEBE SER COMILLAS SENCILLAS, DE LO CONTRARIO DA ERROR
SELECT DISTINCT airline
    FROM  {{ref('flight_logs')}}
    WHERE aircraft_type = '{{var("tipo_de_avion")}}' AND 
          airline IS NOT NULL 
LIMIT {{var('maximos_registros')}}
```

# EJECUTAR EL MODELO
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt run --models modelo_8_usando_variables_dbt_project

- models.dbt_poc.example
21:16:34  Found 8 models, 7 tests, 2 snapshots, 0 analyses, 310 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
21:16:34
21:16:34  Concurrency: 1 threads (target='dev')
21:16:34
21:16:34  1 of 1 START sql view model public.vista_usando_variables ...................... [RUN]
21:16:35  1 of 1 OK created sql view model public.vista_usando_variables ................. [CREATE VIEW in 0.18s]
21:16:35
21:16:35  Finished running 1 view model in 0 hours 0 minutes and 0.52 seconds (0.52s).
21:16:35
21:16:35  Completed successfully
```
<img src="imagenes\variables_desde_dbt_project.png">



# USANDO ANALYSES

# ADICIONAR UN NUEVO MODELO
### dentro de la carpeta analyses/ adicionar un archivo .sql  y adicionar el codigo del ejemplo 

```yaml
analyses/analyses_test.sql
```

```
⭐ dbt_poc [project_directory]
┗ 🌼 seeds [package]
  ┗ 📚flight_logs.csv
┗ 🌞 models [package]
  ┗ ⚜️ schema.yaml
  ┗ ♻️ sources.yaml
  ┗ 🦔 src
    ┗ modelo_1_vista_query_directo.sql
    ┗ modelo_2_tabla_query_con_with_renombrando_columnas.sql
    ┗ modelo_3_tabla_incremental_nombre_personalizado_uso_script_de_referencia.sql
    ┗ modelo_4_tabla_incremental_usando_join.sql
    ┗ modelo_5_tabla_usando_el_alias_del_source.sql
    ┗ modelo_6_set_1_con_jinja.sql
    ┗ modelo_7_usar_macro.sql
    ┗ modelo_8_usando_variables_dbt_project.sql
  ┗ 📸 snapshots [package]
    ┗ snapshot_1_tabla_validar_multi_campos.sql   
    ┗ snapshot_2_tabla_validar_todos_los_campos.sql
  ┗ 🚀 test [package]
    ┗ test_1_verificar_que_no_hay_menores_de_edad.sql
    ┗ test_2_verificar_que_salen_vuelos_desde_o_hacia_xanadu.sql
    ┗ test_3_check_null_values_desde_el_macro.sql
  ┗ 🦄 macros
    ┗ macro_sin_valores_nulos.sql
    ┗ macro_validar_adultos_mayores.sql
    ┗ macro_filro_con_set.sql
  ┗ 🔑 dbt_project.yml
┗ ☢️ analyses [package]
  ┗ analyses_test.sql
```

# CODIGO DE EJEMPLO

```sql
{% set seat_numbers = ('A1', 'B2', 'C3') %}

WITH result_table AS (
  SELECT *
    FROM  {{ref('flight_logs')}}
  WHERE seat_number IN {{ seat_numbers }}
    LIMIT 5
)

SELECT *
FROM result_table
```

# COMPILAR EL ANALYSES
## VEMOS QUE RETORNA EL QUERY LIMPIO, CON LOS VALORES DE REEMPLAZO DE LAS VARIABLES
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt compile --select analyses_test

- models.dbt_poc.example
04:16:32  Found 8 models, 7 tests, 2 snapshots, 1 analysis, 310 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
04:16:32
04:16:32
04:16:32  Compiled node 'analyses_test' is:

WITH result_table AS (
  SELECT *
    FROM  "postgres"."public"."flight_logs"
  WHERE seat_number IN ('A1', 'B2', 'C3')
    LIMIT 5
)

SELECT *
FROM result_table
```

# EL QUERY QUEDA ALMACENADO EN 
## .\target\compiled\dbt_poc\analyses\analyses_test.sql
# SE PUEDE VALIDAR EL QUERY GENERADO ABRIENDO EL ARCHIVO .sql Y EJECUTANDOLO EN LA BASE DE DATOS.







# DOCUMENTACION
# GENERAR EL JSON DE LA DOCUMENTACION
```yaml
(venv) jorge@cardona/dbt_poc:~$ dbt docs generate
- models.dbt_poc.example
23:14:11  Found 8 models, 7 tests, 2 snapshots, 0 analyses, 310 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
23:14:11
23:14:11  Concurrency: 1 threads (target='dev')
23:14:11  
--- El valor de seat_numbers es: ('A1', 'B2', 'C3')
23:14:11  
23:14:11  *** El valor de seat_numbers es: ('A1', 'B2', 'C3')
23:14:11
23:14:12  Building catalog
23:14:12  Catalog written to C:\Users\QiDimMak\Desktop\dbt postgres\dbt_poc\target\catalog.json
```

# INICIAR EL SERVIDOR LOCAL PARA ACCEDER A LA DOCUMENTACION
```
(venv) jorge@cardona/dbt_poc:~$ dbt docs serve
- models.dbt_poc.example
23:14:11  Found 8 models, 7 tests, 2 snapshots, 0 analyses, 310 macros, 0 operations, 1 seed file, 4 sources, 0 exposures, 0 metrics, 0 groups
23:14:11
23:14:11  Concurrency: 1 threads (target='dev')
23:14:11  
--- El valor de seat_numbers es: ('A1', 'B2', 'C3')
23:14:11  
23:14:11  *** El valor de seat_numbers es: ('A1', 'B2', 'C3')
23:14:11
23:14:12  Building catalog
23:14:12  Catalog written to C:\Users\QiDimMak\Desktop\dbt postgres\dbt_poc\target\catalog.json
(venv) PS C:\Users\QiDimMak\Desktop\dbt postgres\dbt_poc> dbt docs serve
23:16:40  Running with dbt=1.5.2
Serving docs at 8080
To access from your browser, navigate to: http://localhost:8080


Press Ctrl+C to exit.
127.0.0.1 - - [13/Jul/2023 18:16:42] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [13/Jul/2023 18:16:42] "GET /manifest.json?cb=1689290202671 HTTP/1.1" 200 -
127.0.0.1 - - [13/Jul/2023 18:16:42] "GET /catalog.json?cb=1689290202671 HTTP/1.1" 200 -
```

# MENU DE LA DOCUMENTACION
## PROYECTO
<img src="imagenes\docs_1.png">

## BASE DE DATOS
<img src="imagenes\docs_2.png">

## Acceso al Gráfico de linaje
<img src="imagenes\docs_3.png">

## Gráfico de linaje
<img src="imagenes\docs_4.png">

## Recursos en el Gráfico de linaje
<img src="imagenes\docs_5.png">

## Vista Recursos del Proyecto
<img src="imagenes\docs_6.png">

# TABLA RESUMEN DE COMANDOS DBT

| Command   | --select  | --exclude | --selector | --defer       | --resource-type | --inline  |
|-----------|-----------|-----------|------------|--------------|-----------------|-----------|
| run       | ✓         | ✓         | ✓          | ✓            |                 |           |
| test      | ✓         | ✓         | ✓          | ✓            |                 |           |
| seed      | ✓         | ✓         | ✓          |              |                 |           |
| snapshot  | ✓         | ✓         | ✓          |              |                 |           |
| ls (list) | ✓         | ✓         | ✓          |              | ✓               |           |
| compile   | ✓         | ✓         | ✓          |              |                 | ✓         |
| freshness | ✓         | ✓         | ✓          |              |                 |           |
| build     | ✓         | ✓         | ✓          | ✓            | ✓               |           |

