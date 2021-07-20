import mysql.connector
import datetime
import emoji
import main
#from scrapy.exceptions import DropItem


class Asin:
    # print("qui")
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
        self.get_asin()

    def get_asin(self): # Estrapolazione degli asin
        try:
            with open("cache/db_name.txt", "r+") as f:
                a = f.read()
            with open("cache/table_name.txt", "r+") as f2:
                b = f2.read()
            with open("cache/file_path.txt", "r+") as f3:
                file_path = f3.read()

            db_table = a+"."+b
            print("Tabella in uso:",db_table)

            self.curr.execute("SELECT MPN FROM %s" % db_table )
            asin = self.curr.fetchall()
            date = datetime.datetime.now()
            # file_name = "asin_" + str(date.strftime("%m_%d_%Y_%H_%M_%S"))
            file_name = str(file_path) + ".txt"
            print("Asin in scrittura nel file: %s" % str(file_name))
            with open(file_name, "w+") as f: #Prima veniva salvato nella cartella asin
                for i in asin:
                    i = str(i)
                    i = i.replace("(", "")
                    i = i.replace(")", "")
                    i = i.replace(",", "")
                    i = i.replace(" ", "")
                    i = i.replace("'", "")
                    f.write(i + "\n")
                    print(i)

            print("Processo finito")
        except Exception as e:
            print("Errore: ",e)


if __name__ == "__main__":
    Asin()