{{ 
config(
		materialized='view', 
		alias='tabla_source'
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