{{ 
config(
		materialized='view', 
		alias='vista_usando_variables'
		) 
}}

SELECT DISTINCT airline
    FROM  {{ref('flight_logs')}}
    WHERE aircraft_type = '{{var("tipo_de_avion")}}' AND 
          airline IS NOT NULL 
LIMIT {{var('maximos_registros')}}