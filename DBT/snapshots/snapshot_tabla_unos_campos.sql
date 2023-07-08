-- target_database='dbt_snapshots'
-- target_schema='dbt_snapshots'
{% snapshot validar_multi_campos_snapshot %}

{{
  config(
    target_database='dbt_snapshots',
    target_schema='dbt_snapshots',
    unique_key='id',
    strategy='check',
    invalidate_hard_deletes=True,
    check_cols=['flight_number', 'airline']
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