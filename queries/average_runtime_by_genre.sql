SELECT tg.genre, AVG(tb.runtimeMinutes)
FROM title_genres tg
JOIN title_basics tb ON tg.tconst = tb.tconst
GROUP BY tg.genre
