-- SQLite

SELECT * FROM Directory;
SELECT name FROM Directory where name = ""

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

/*THIS COMMAND DELETES EVERY TABLE BUT THE DIRECTORY TABLE*/
PRAGMA writable_schema = 1;
DELETE FROM sqlite_master WHERE type = 'table' AND name NOT IN ('Directory');
PRAGMA writable_schema = 0;
VACUUM;

ALTER TABLE Directory
ADD COLUMN press_release_layout;

UPDATE Directory SET general_pressrelease_link = 'https://williams.house.gov/media-center/press-releases' where id = 391;