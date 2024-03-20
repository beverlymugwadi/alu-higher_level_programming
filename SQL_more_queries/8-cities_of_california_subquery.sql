-- List cities in California
SELECT name, id FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = 'California') ORDER BY id;
