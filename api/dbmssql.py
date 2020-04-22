import _mssql
import pymssql

server = 'nbashots.database.windows.net'
database = 'nbashotsdb'
user = 'group2-4'
password = 'Rootbeer24'
cnxn = pymssql.connect(server, user, password, database)
cursor = cnxn.cursor()

cursor.execute("SELECT COUNT(*) FROM dbo.nba_shots_cleaned")  
count = list(cursor)
print(count)
print(count[0][0])
conn.close()
