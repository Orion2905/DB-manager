CREATE TABLE db.disponibili LIKE db.amazon_it; -- Per cambiare la tabella da elaborare cambiare "amazon_it"
INSERT INTO db.disponibili SELECT * FROM db.amazon_it where SoldBy >= '1' and Available = '1' and Price >'0' and eBayCategory = 'articoli per cani';
-- IMPORTANTE : prima di lancaire al query eliminare le tabelle "disponibili_no_doppioni" e "disponibili"
-- Crea tabella finale
CREATE TABLE db.disponibili_doppioni LIKE db.disponibili; 
INSERT INTO db.disponibili_doppioni SELECT * FROM db.disponibili;

-- step 1
CREATE TABLE db.temp LIKE db.disponibili_doppioni;

-- step 2
INSERT INTO db.temp SELECT * FROM db.disponibili_doppioni GROUP BY db.disponibili_doppioni.Title; -- Per mettere il titolo basta sostituire MPN con Title

-- step 3
DROP TABLE db.disponibili_doppioni;

ALTER TABLE db.temp RENAME TO db.disponibili_no_doppioni;