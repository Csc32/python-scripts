import mariadb
import pandas as pd
'''
read the csv and save data in a 
variable
'''
csv = pd.read_csv("./casas macro 5A.csv",header=0) 
data =  []
# connect with the data base;
try:
   conn =  mariadb.connect(
           user = "phpmyadmin",
           password = "root",
           host = "localhost",
           port = 3306,
           database = "database"
           )
except Exception as e:
    print(f"Error to connect: {e}")
    raise e

cur = conn.cursor()
query = "INSERT INTO casa(numero_casa, fk_macro_id) VALUES(%s,%s)"
for i,row in csv.iterrows():
    id_macro = row["fk_macro_id"] 
    casa = row["numero_casa"]
    tempData = (casa,id_macro)
    data.append(tempData)

print(data)
cur.executemany(query,data)


conn.commit()
conn.close()
print("Save data in array")
