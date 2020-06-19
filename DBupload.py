import MySQLdb
import csv
import os

print("RUNNING")

user = '' # your username
passwd = '' # your password
host = '' # your host or localhost if running locally
db = '' # database where your table is stored
dest_folder = '' # destination folder for the files to be written

try:
    con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db, autocommit=True)
    cursor = con.cursor()
except (MySQLdb.Error, MySQLdb.Warning):  # catch relevant exceptions
    raise ConnectionError

for fileName in os.listdir(''): #update this path
    if not fileName.lower().endswith('.py'):  # check for proper file type
        name = os.path.splitext(fileName)
        tableName = name[0]
        tableFile = open(fileName)
        csv_data = csv.DictReader(tableFile, dialect='excel')
        insert_sql = 'insert into ' + tableName + ' (' + ','.join(csv_data.fieldnames) + ') VALUES (' + ','.join(
            ['%s'] * len(csv_data.fieldnames)) + ')'
        values = []
        for row in csv_data:
            row_values = []
            for field in csv_data.fieldnames:
                row_values.append(row[field])
            values.append(row_values)
        print(insert_sql, values)
        cursor.executemany(insert_sql, values)

# close the connection to the database.
cursor.close()
print("Done")
