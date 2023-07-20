{% macro hook_postprocesamiento() %}
  {% set current_timestamp = target.timestamp %}
  {% set message = "HOOK POST PROCESAMIENTO,Finaliza ejecución de DBT a las " ~ current_timestamp %}
  {# LLAMO UN MACRO DESDE OTRO MACRO #}
  {% do mostrar_mensaje(message) %}
{% endmacro %}