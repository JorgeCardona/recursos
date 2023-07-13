SELECT CASE
    WHEN (
            SELECT COUNT(*) 
                FROM {{ ref('flight_logs') }}
            WHERE passenger_age < 18
          ) > 0 THEN 
                    NULL
    ELSE
        RAISE EXCEPTION 'HAY MENORES DE EDAD EN EL VUELO'
END