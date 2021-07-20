import mysql.connector
import datetime
#from scrapy.exceptions import DropItem


class Clean:

    def __init__(self): # Connessione al database
        with open("cache/connection.txt", "r+") as f:
            lines = f.readlines()
            # HOST
            host = lines[0].split('=')
            host = host[1]
            host = host.replace("'", "")
            host = host.replace("\n", "")
            host = host.replace(",", "")
            # USER
            user = lines[1].split('=')
            user = user[1]
            user = user.replace("'", "")
            user = user.replace("\n", "")
            user = user.replace(",", "")
            # PORT
            port = lines[2].split('=')
            port = port[1]
            port = port.replace("'", "")
            port = port.replace("\n", "")
            port = port.replace(",", "")
            # PASSWORD
            passwd = lines[3].split('=')
            passwd = passwd[1]
            passwd = passwd.replace("'", "")
            passwd = passwd.replace("\n", "")
            passwd = passwd.replace(",", "")
            # DATABASE
            db = lines[4].split('=')
            db = db[1]
            db = db.replace("'", "")
            db = db.replace("\n", "")
            db = db.replace(",", "")
            # print(host, user, port, passwd, db)

        self.conn = mysql.connector.connect(
            host=str(host),
            user=str(user),
            port=str(port),
            passwd=str(passwd),
            database=str(db)
        )
        self.curr = self.conn.cursor()
        self.clean()

    def clean(self): # Elaborazione della tabella amazon_it
        print("Processo iniziato...")
        with open("cache/category.txt", "r+") as f:
            cat = f.read()
            print("Categoria selezionata:", cat)

        sql = "CREATE TABLE db.disponibili LIKE db.amazon_it;"
        self.curr.execute(sql)
        sql_2 = "INSERT INTO db.disponibili SELECT * FROM db.amazon_it where SoldBy >= '1' and Available = '1' and Price >'0' and eBayCategory = '%s';" % cat
        self.curr.execute(sql_2)
        self.conn.commit()
        sql_3 = "CREATE TABLE db.disponibili_doppioni LIKE db.disponibili;"
        self.curr.execute(sql_3)
        sql_4 = "INSERT INTO db.disponibili_doppioni SELECT * FROM db.disponibili;"
        self.curr.execute(sql_4)
        self.conn.commit()
        sql_5 = "CREATE TABLE db.temp LIKE db.disponibili_doppioni;"
        self.curr.execute(sql_5)
        sql_6 = "INSERT INTO db.temp SELECT * FROM db.disponibili_doppioni GROUP BY db.disponibili_doppioni.Title;"
        self.curr.execute(sql_6)
        self.conn.commit()
        sql_7 = "DROP TABLE db.disponibili_doppioni;"
        self.curr.execute(sql_7)
        sql_8 = "ALTER TABLE db.temp RENAME TO db.disponibili_no_doppioni;"
        self.curr.execute(sql_8)
        print("Processo terminato")
