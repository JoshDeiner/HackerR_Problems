SELECT city, length(city) AS city_length
FROM station
ORDER BY city_length, city ASC LIMIT 1;


SELECT city, length(city) AS city_length
FROM station
ORDER BY city_length DESC, city ASC LIMIT 1;
