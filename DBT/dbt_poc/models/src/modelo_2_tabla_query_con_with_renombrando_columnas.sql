{{ 
config(
		materialized='table', 
		sort='flight_number', 
		dist='id'
		) 
}}

WITH EJEMPLO_SELECT_WITH AS (
  SELECT
    id AS ID,
    flight_number AS FLIGHT_CODE,
    airline AS CARRIER,
    departure_airport AS ORIGINATING_AIRPORT,
    departure_gate AS BOARDING_GATE,
    departure_city AS ORIGINATING_CITY,
    departure_country AS ORIGINATING_COUNTRY
  FROM public.flight_logs
)

SELECT * 
FROM EJEMPLO_SELECT_WITH
ORDER BY FLIGHT_CODE