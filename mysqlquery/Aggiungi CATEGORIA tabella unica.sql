-- Aggiunge la nuova categoria
INSERT IGNORE
	INTO db.tabella_unica
SELECT *
	FROM db.disponibili_no_doppioni;