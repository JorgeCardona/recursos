-- macros/sql/validation_macros.sql

{% macro check_null_values(model) %}
 SELECT * FROM {{ model }} WHERE
 {% for col in adapter.get_columns_in_relation(model) -%} # -% significa que elimina los espacios en blancodel final trim
 {{ col.column }} IS NULL OR
 {% endfor %}
 FALSE
{% endmacro %}
