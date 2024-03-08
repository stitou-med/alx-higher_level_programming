-- Lists all records of the table second_table.
-- Won't list row without `name` value
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
