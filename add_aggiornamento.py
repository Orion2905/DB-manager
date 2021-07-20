import mysql.connector
import datetime
#from scrapy.exceptions import DropItem


class Add_agg:

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
        self.add()

    def add(self): # Aggiunta categoria
        self.curr.execute("""INSERT IGNORE INTO db.tabella_unica SELECT * FROM aggiornamento.amazon_it;""")
        self.conn.commit()
        print("Aggiornamento aggiunto")