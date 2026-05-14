import sqlite3


con = sqlite3.connect("Harvester.db")
cursor = con.cursor()

# cursor.execute("select * FROM sqlite_master where type='table';")
cursor.execute("select * FROM Artic_Table")
rows = cursor.fetchall()

for row in rows:
    print(row)

