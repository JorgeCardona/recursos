{{ 
config(
		materialized='view', 
		alias='vista_hooks',
        pre_hook= "{{ hook_preprocesamiento() }}",
        post_hook="{{ hook_postprocesamiento() }}"
		) 
}}

SELECT DISTINCT airline
    FROM  {{ref('flight_logs')}}
    WHERE aircraft_type = '{{var("tipo_de_avion")}}' AND 
          airline IS NOT NULL 
LIMIT {{var('maximos_registros')}}