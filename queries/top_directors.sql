SELECT nb.nconst, nb.primaryName,
COUNT(*) as num_highly_rated_films, RANK() OVER (ORDER BY COUNT(*) DESC) as rank

FROM title_ratings tr
JOIN title_basics tb ON tr.tconst=tb.tconst
JOIN title_crew tc ON tb.tconst=tc.tconst
JOIN name_basics nb ON nb.nconst = tc.directors

WHERE tr.numVotes>5000
    AND tr.averageRating>=8.0
    AND (tb.titleType IN ('movie','short'))
    AND tb.isAdult = 0

GROUP BY nb.nconst, nb.primaryName, nb.knownForTitles
LIMIT 25
