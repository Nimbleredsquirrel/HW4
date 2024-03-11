CREATE TABLE requests_log (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    country VARCHAR(255),
    year INT,
    trees_count INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE OR REPLACE FUNCTION most_frequent_city() RETURNS TABLE(city VARCHAR, queries_count INT) AS $$ BEGIN RETURN QUERY
SELECT city,
    COUNT(*) as queries_count
FROM requests_log
GROUP BY city
ORDER BY queries_count DESC
LIMIT 1;
END;
$$ LANGUAGE plpgsql;