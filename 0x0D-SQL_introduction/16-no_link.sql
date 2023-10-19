-- Lists all records second_table with atrribute name.
SELECT `score`, `name` FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
