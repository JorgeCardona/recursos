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