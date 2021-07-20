-- Crea la tabella unica
CREATE TABLE db.tabella_unica LIKE db.amazon_it;
INSERT INTO db.tabella_unica SELECT * FROM db.disponibili_no_doppioni;

-- Unisce la tabella aggiornamento e disponibili
INSERT IGNORE
	INTO db.tabella_unica
SELECT *
	FROM aggiornamento.amazon_it;