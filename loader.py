import psycopg2
from os import environ

class DatabaseLoader():
    #main function
    def __init__(self):
        server  = environ.get("server")
        user = environ.get("user")
        password = environ.get("password")
        dbname = environ.get("dbname")
        self.setupDb(server, user, password, dbname)

    #takes the csv and inserts it into the db
    def setupDb(self, server, user, password, dbname):
        print(server)
        print(user)
        print(password)
        print(dbname)
        conn = psycopg2.connect("host=" + str(server) + " port='5432' dbname=" + str(dbname) + " user=" + str(user) + " password=" + str(password))
        cur = conn.cursor()

        # does table exist
        tb_exists = "select exists(select relname from pg_class where relname='" + "wine_reviews" + "')"
        print(tb_exists)
        cur.execute(tb_exists)
        execute = cur.fetchone()[0]
        if not execute:
            # make table
            cur.execute(
                'create table wine_reviews(country VARCHAR, designation VARCHAR, points INT, price VARCHAR, province VARCHAR, region_1 VARCHAR, region_2 VARCHAR, variety VARCHAR, winery VARCHAR);')
            conn.commit()
        # copy csv
        print('added data')
        f = open(r'/opt/app-root/src/wineData.csv', 'r')
        cur.copy_from(f, "wine_reviews", sep=',')
        conn.commit()
        f.close()
        print('finished script')


if __name__ == '__main__':
    DatabaseLoader()
