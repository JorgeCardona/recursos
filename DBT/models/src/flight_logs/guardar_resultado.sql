{% set get_generos_registrados %}
  SELECT DISTINCT passenger_gender
    FROM  {{ref('flight_logs')}}
    WHERE passenger_gender IS NOT NULL -- evita que retorne valores nulos
{% endset %}

{% set results = run_query(get_generos_registrados) %}

{% do log(print("--- El query es: " ~ get_generos_registrados), info=True) %}

{% if execute %}
    {# Return the first column #}
    {% set results_list = results.columns[0].values() %}
{% else %}
    {% set results_list = [] %}
{% endif %}

-- VER EL LOG SIN LA FECHA a la izquierda en la salida estándar
{% do log(print("--- El valor de results_list es: " ~ results_list), info=True) %}

# hacer el query con los valores filtrados
WITH result_table AS (
  SELECT *
    FROM  {{ref('flight_logs')}}
  WHERE passenger_gender IN {{ results_list }}
    LIMIT 10
)

SELECT *
FROM result_table

