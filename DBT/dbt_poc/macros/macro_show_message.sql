{% macro mostrar_mensaje(message) %}
  {% do log(print(message), info=True) %}
{% endmacro %}