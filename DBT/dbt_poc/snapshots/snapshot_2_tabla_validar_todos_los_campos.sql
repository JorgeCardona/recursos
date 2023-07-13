{% snapshot validar_todos_los_campos_snapshot %}

{{
  config(
    target_database='postgres',
    target_schema='dbt_snapshots_todos_los_campos',
    unique_key='id',
    strategy='check',
    invalidate_hard_deletes=True,
    check_cols='all'
  )
}}

SELECT
  id,
  secure_code,
  flight_number,
  airline,
  departure_airport
FROM {{ source('fuente_original','tabla_original') }}
WHERE id = 1

{% endsnapshot %}