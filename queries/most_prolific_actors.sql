SELECT tp.nconst, nb.primaryName, COUNT(DISTINCT tp.tconst)
FROM title_principals tp
JOIN name_basics nb ON nb.nconst=tp.nconst
JOIN title_basics tb ON tp.tconst=tb.tconst
WHERE tp.category IN ('actor', 'actress') AND tb.isAdult = 0
    AND tb.titleType='movie' AND tb.runtimeMinutes >= 40
GROUP BY tp.nconst
ORDER BY COUNT(*) DESC
LIMIT 15
