SELECT CASE
    WHEN (
            SELECT COUNT(*) 
                FROM {{ ref('flight_logs') }}
            WHERE 'XANADU' IN (departure_city, arrival_city)
          ) > 0 THEN 
                    NULL
    ELSE
        RAISE EXCEPTION 'NO EXISTEN VUELOS DE O HACIA XANADU'
END