import mysql.connector
import datetime
import main
#from scrapy.exceptions import DropItem


class SaveCSV:
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
        self.save()

    def save(self): # Estrapolazione degli asin
        try:
            with open("cache/db_name.txt", "r+") as f:
                a = f.read()
            with open("cache/table_name.txt", "r+") as f2:
                b = f2.read()

            db_table = a+"."+b
            print("Tabella in uso:",db_table)

            self.curr.execute("SELECT MPN FROM %s" % db_table )
            asin = self.curr.fetchall()
            date = datetime.datetime.now()
            file_name = "asin_" + str(date.strftime("%m_%d_%Y_%H_%M_%S"))
            print("Asin in scrittura nel file: %s" % str(file_name))
            with open("asin/" + file_name + "txt", "w") as f:
                for i in asin:
                    i = str(i)
                    i = i.replace("(", "")
                    i = i.replace(")", "")
                    i = i.replace(",", "")
                    i = i.replace(" ", "")
                    i = i.replace("'", "")
                    f.write(i + "\n")
                    print(i)
        except Exception as e:
            print("Errore: ",e)


if __name__ == "__main__":
    SaveCSV()