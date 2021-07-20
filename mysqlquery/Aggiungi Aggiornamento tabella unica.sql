-- Aggiunge nella tabella "tabella_unica" i dati dell'aggiornamento
INSERT IGNORE
	INTO db.tabella_unica
SELECT *
	FROM aggiornamento.amazon_it;