import psycopg2



conn = psycopg2.connect(
    host="86.252.168.180",
    database="postgres",
    user="postgres",
    password="postgres")

cur = conn.cursor()

resource = 'test2'

cur.execute('CREATE TABLE ' + resource + '(date date,prix_100 integer NULL,prix_10 integer NULL,prix_1 integer NULL)')
conn.commit()

cur.execute('SELECT * from test')
version = cur.fetchall()
print("resultat")
print(version)

cur.close()
conn.close()
print("La connexion PostgreSQL est fermée")