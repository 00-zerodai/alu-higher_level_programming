-- List names and scores of records scoring at least 10.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
