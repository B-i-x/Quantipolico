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

ALTER TABLE Directory
ADD COLUMN title_layout;

UPDATE Directory SET general_pressrelease_link = 'https://jayapal.house.gov/category/news/' where id = 426;

UPDATE Directory SET general_pressrelease_link = 'https://clyde.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 125;
UPDATE Directory SET general_pressrelease_link = 'https://cherfilus-mccormick.house.gov/media/press-releases' where id = 109;
UPDATE Directory SET general_pressrelease_link = 'https://matsui.house.gov/media/press-releases' where id = 28;

UPDATE Directory SET general_pressrelease_link = 'https://mcclain.house.gov/press-releases' where id = 211;
UPDATE Directory SET general_pressrelease_link = 'https://davis.house.gov/media' where id = 142;

UPDATE Directory SET general_pressrelease_link = 'https://watsoncoleman.house.gov/newsroom/press-releases' where id = 257;

UPDATE Directory SET general_pressrelease_link = 'https://grijalva.house.gov/category/congress_press_release/' where id = 12;

UPDATE Directory SET general_pressrelease_link = 'https://hayes.house.gov/press-releases' where id = 87;

DELETE FROM Directory WHERE id = 400;

UPDATE Directory SET general_pressrelease_link = 'https://teddeutch.house.gov/press' where id = 111;
UPDATE Directory SET general_pressrelease_link = 'https://newman.house.gov/press' where id = 138;

UPDATE Directory SET general_pressrelease_link = 'https://carey.house.gov/media/press-releases' where id = 317;
UPDATE Directory SET general_pressrelease_link = 'https://joyce.house.gov/press' where id = 316;
UPDATE Directory SET general_pressrelease_link = 'https://ritchietorres.house.gov/press' where id = 275;

UPDATE Directory SET general_pressrelease_link = 'https://mcmorris.house.gov/press' where id = 424;
UPDATE Directory SET general_pressrelease_link = 'https://nehls.house.gov/press' where id = 388;

UPDATE Directory SET general_pressrelease_link = 'https://mooney.house.gov/category/press-releases/' where id = 431;

UPDATE Directory SET general_pressrelease_link = 'https://cheney.house.gov/category/press_release/' where id = 441;

UPDATE Directory SET press_release_layout = 'date_div_2' where id = 441;

UPDATE Directory SET general_pressrelease_link = 'https://guthrie.house.gov/news/documentquery.aspx?DocumentTypeID=2381' where id = 172;

UPDATE Directory SET general_pressrelease_link = 'https://timmons.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 353;

UPDATE Directory SET general_pressrelease_link = 'https://phillips.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 218;
UPDATE Directory SET general_pressrelease_link = 'https://jackson.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 379;

UPDATE Directory SET general_pressrelease_link = 'https://pfluger.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 377;

UPDATE Directory SET general_pressrelease_link = 'https://mikegarcia.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 47;
UPDATE Directory SET general_pressrelease_link = 'https://carter.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 397;
UPDATE Directory SET general_pressrelease_link = 'https://valadao.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 43;
UPDATE Directory SET general_pressrelease_link = 'https://neal.house.gov/news/documentquery.aspx?DocumentTypeID=27' where id = 193;
UPDATE Directory SET general_pressrelease_link = 'https://chrissmith.house.gov/news/documentquery.aspx?Year=2022' where id = 249;

UPDATE Directory SET general_pressrelease_link = 'https://connolly.house.gov/news/documentquery.aspx?DocumentTypeID=1952' where id = 418;


SELECT id, general_pressrelease_link FROM Directory  WHERE  next_page_control  IS NULL;

UPDATE Directory SET next_page_control = 'double_next' where id = 97;
