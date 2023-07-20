{% macro hook_preprocesamiento() %}
  {% set current_timestamp = target.timestamp %}
  {% set message = "HOOK PRE PROCESAMIENTO, Inicio de ejecución de DBT a las " ~ current_timestamp %}
  {# LLAMO UN MACRO DESDE OTRO MACRO #}
  {% do mostrar_mensaje(message) %}
{% endmacro %}