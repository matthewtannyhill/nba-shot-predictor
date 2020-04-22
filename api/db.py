import pyodbc
server = 'nbashots.database.windows.net'
database = 'nbashotsdb'
username = 'group2-4'
password = 'Rootbeer24'
driver= '{ODBC Driver 17 for SQL Server}'
#conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=yourserver.yourcompany.com;PORT=1433;DATABASE=yourdb;UID=user;PWD=password;TDS_VERSION=7.2')
cnxn = pyodbc.connect('DRIVER=FreeTDS;SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password +'TDS_VERSION=7.2')
cursor = cnxn.cursor()

cursor.execute("SELECT TOP 100 * FROM dbo.nba_shots_cleaned")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]) + " " + str(row[6]) + " " + str(row[7]))
    row = cursor.fetchone()

cnxn.commit()