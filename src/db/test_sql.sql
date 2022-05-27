-- SQLite

SELECT * FROM Directory;


/*
INSERT INTO Directory (name) VALUES ("poop");
*/

/*
DELETE FROM Directory WHERE name = "poop";
*/

/*
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='DIRECTORY';
*/

SELECT name FROM Directory WHERE general_pressrelease_link IS NULL ORDER BY id ASC LIMIT 10;

SELECT * FROM Directory ORDER BY id DESC LIMIT 1;