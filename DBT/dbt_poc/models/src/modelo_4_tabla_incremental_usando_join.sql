{{ 
config(
		materialized='incremental', 
		incremental_strategy = 'delete+insert',
		alias='tabla_join'
		) 
}}

WITH SELECT_JOIN AS (
    SELECT T1.* FROM {{ref('modelo_1_vista_query_directo')}} AS T1
	inner JOIN {{ref('modelo_2_tabla_query_con_with_renombrando_columnas')}} AS T2
	ON T1.id = T2.ID
)

SELECT * FROM SELECT_JOIN
LIMIT 10