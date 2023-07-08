SELECT * FROM 
{{ ref('flight_logs') }}
WHERE passenger_age < 18
LIMIT 10