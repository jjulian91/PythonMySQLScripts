import MySQLdb
import csv


print("RUNNING")
user = 'root' # your username
passwd = 'dBPJJWa4gkBjBQZn' # your password
host = 'localhost' # your host or localhost if running locally
db = 'chefables' # database where your table is stored
dest_folder = 'C:\\Users\\jonju\\Desktop\\Chefables\\DB Tables\\' # destination folder for the files to be written
try:
    con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
    cursor = con.cursor()
except:
    raise(ConnectionError)

query = 'SHOW TABLES'
cursor.execute(query)
listOfTables = cursor.fetchall()
tableNames = [i[0] for i in listOfTables]

for name in tableNames:
    if 'ref_' in name:
        '''Only pulls the Ref_tables'''
        cursor.execute("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='"+name+"'")
        columnTuples = cursor.fetchall()
        ColumnNames = [i[0] for i in columnTuples]
        '''
        Opens instance and writes list as a row
        '''
        with open(dest_folder + name + '.csv','w') as f:
            writer = csv.writer(f,delimiter=',')
            writer.writerow(ColumnNames)