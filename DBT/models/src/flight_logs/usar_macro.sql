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

# hacer el query con los valores filtrados
WITH result_table AS (
  SELECT *
    FROM  {{ref('flight_logs')}}
  WHERE passenger_gender IN {{ results_list}}
    LIMIT 10
)

SELECT *
FROM result_table