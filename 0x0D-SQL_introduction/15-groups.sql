-- count matches in score
SELECT score, count(*) AS number FROM second_table GROUP BY score DESC;
