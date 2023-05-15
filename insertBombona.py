import mariadb
import pandas as pd 

# connect with the data base;
try:
   conn =  mariadb.connect(
           user = "username",
           password = "your_password",
           host = "your_host",
           port = 0, #your port
           database = "database_name"
           )
except Exception as e:
    print(f"Error to connect: {e}")
    raise e
cur = conn.cursor(); 
query =  "SELECT * FROM casa"
cur.execute(query)
houses = cur.fetchall()

bombonas = "SELECT * FROM bombona"
cur.execute(bombonas)
resultBom = cur.fetchall()
data = []
for house in houses:
    for  bombona in resultBom:
        data.append((house[0],bombona[0], 0))

insertQuery = "INSERT INTO casas_bombonas(fk_casa_id, fk_bombona_id, cantidad_bombona) VALUES(%s, %s, %s)"

cur.executemany(insertQuery,data)
conn.commit()
conn.close()
