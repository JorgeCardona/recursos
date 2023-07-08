{% test tercera_edad(model, column_name) %}
SELECT
 *
FROM
 {{ model }}
WHERE
 {{ column_name}} > 80
{% endtest %}
