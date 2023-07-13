{{ 
config(
		materialized='incremental', 
		alias='tabla_incremental'
		) 
}}

WITH SELECT_TEST AS (
    SELECT * FROM {{ref('modelo_2_tabla_query_con_with_renombrando_columnas')}}
)

SELECT * FROM SELECT_TEST