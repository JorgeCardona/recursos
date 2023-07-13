SELECT id,
		flight_number, 
		airline, 
		departure_airport,
		departure_gate,
		departure_city, 
		departure_country
FROM public.flight_logs
ORDER BY flight_number