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

UPDATE Directory SET general_pressrelease_link = 'https://jayapal.house.gov/category/news/' where id = 426;

UPDATE Directory SET general_pressrelease_link = 'https://clyde.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 125;
UPDATE Directory SET general_pressrelease_link = 'https://cherfilus-mccormick.house.gov/media/press-releases' where id = 109;
UPDATE Directory SET general_pressrelease_link = 'https://matsui.house.gov/media/press-releases' where id = 28;

UPDATE Directory SET general_pressrelease_link = 'https://mcclain.house.gov/press-releases' where id = 211;
UPDATE Directory SET general_pressrelease_link = 'https://davis.house.gov/media' where id = 142;

UPDATE Directory SET general_pressrelease_link = 'https://watsoncoleman.house.gov/newsroom/press-releases' where id = 257;

UPDATE Directory SET general_pressrelease_link = 'https://grijalva.house.gov/category/congress_press_release/' where id = 12;

UPDATE Directory SET general_pressrelease_link = 'https://hayes.house.gov/press-releases' where id = 87;

DELETE FROM Directory WHERE id = 279;

UPDATE Directory SET general_pressrelease_link = 'https://teddeutch.house.gov/press' where id = 111;
UPDATE Directory SET general_pressrelease_link = 'https://newman.house.gov/press' where id = 138;

UPDATE Directory SET general_pressrelease_link = 'https://carey.house.gov/media/press-releases' where id = 317;
UPDATE Directory SET general_pressrelease_link = 'https://joyce.house.gov/press' where id = 316;
UPDATE Directory SET general_pressrelease_link = 'https://ritchietorres.house.gov/press' where id = 275;

UPDATE Directory SET general_pressrelease_link = 'https://mcmorris.house.gov/press' where id = 424;
UPDATE Directory SET general_pressrelease_link = 'https://nehls.house.gov/press' where id = 388;

UPDATE Directory SET general_pressrelease_link = 'https://mooney.house.gov/category/press-releases/' where id = 431;
