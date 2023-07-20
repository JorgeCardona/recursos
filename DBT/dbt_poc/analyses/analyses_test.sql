{% set seat_numbers = ('A1', 'B2', 'C3') %}

WITH result_table AS (
  SELECT *
    FROM  {{ref('flight_logs')}}
  WHERE seat_number IN {{ seat_numbers }}
    LIMIT 5
)

SELECT *
FROM result_table