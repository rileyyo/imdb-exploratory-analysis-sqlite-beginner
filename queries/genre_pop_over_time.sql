SELECT tg.genre, CAST(FLOOR(endYear / 10) * 10 AS INTEGER) || 's' AS decade, ROUND(AVG(tr.averageRating), 2) AS average_rating, SUM(tr.numVotes) as total_votes
FROM title_genres tg
JOIN title_basics tb ON tg.tconst = tb.tconst
JOIN title_ratings tr ON tr.tconst = tb.tconst
WHERE tg.genre != 'None' AND decade != 'None'
GROUP BY tg.genre, decade
ORDER BY tg.genre, decade;
