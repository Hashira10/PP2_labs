import psycopg2
import csv


conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=t10o10.10")
cur = conn.cursor()

# upload data from csv file
with open('table.csv', 'r', encoding="utf-8") as f:
    next(f)
    cur.copy_from(f, 'phone_book', sep=' ')
conn.commit()

# entering user name, phone from console
name = input()
num = input()
data = (name, num)
SQL = "INSERT INTO phone_book VALUES (%s, %s);" 
cur.execute(SQL, data) 
conn.commit()

# change user first name
name1 = input()
num1 = input()
data1 = (name1,num1)
sql1 = "UPDATE phone_book SET firstname = %s WHERE phonenumber = %s"
cur.execute(sql1,data1)
conn.commit()

# Querying data from the tables (with different filters)
cur.execute("SELECT firstname, phonenumber FROM phone_book")
rows = cur.fetchall() # for all rows
print(rows)
'''
rows = cur.fetchone() # for one row
print(rows)
rows = cur.fetchmany(3) # for 3 rows
print(rows) 
'''
# Implement deleting data from tables by username of phone
username_of_phone = input()
data = (username_of_phone,)
sql = "DELETE FROM phone_book WHERE firstname=%s"
cur.execute(sql,data)
conn.commit()

conn.close()