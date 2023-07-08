{{ 
config(
		materialized='table', 
		sort='flight_number', 
		dist='id'
		) 
}}

SELECT id,
		flight_number, 
		airline, 
		departure_airport,
		departure_gate,
		departure_city, 
		departure_country
FROM test_poc.flight_logs
ORDER BY flight_number