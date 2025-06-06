SELECT title,country,release_year,type FROM netflix_titles
WHERE type = 'Movie' AND release_year >= 2015 AND country IS NOT NULL;