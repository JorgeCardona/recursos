{%- macro  filtrar_valores_usando_un_macro(query) -%}
    {%- set filtrar -%}
        {{query}}
    {%- endset -%}

    {% do log(print("--- El query a ejecutar es: " ~ filtrar), info=True) %}
    {%- set resultado_query = run_query(filtrar) -%}

    {%- if execute -%}
        {# Return the first column #}
        {% set results_list = resultado_query.columns[0].values() %}
    {%- else -%}
        {% set results_list = [] %}
    {%- endif -%}
    
{% do log(print("--- El valor de results_list del query es: " ~ results_list), info=True) %}

{{results_list}} {# esto hace las veces de retorno de variables {{nombre_de_la_variable_a_retornar}}, sino queda como retorno vacio #}
{% endmacro %}