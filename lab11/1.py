import psycopg2 
import csv 
import re 
 
function = int(input('1-returns all records based on a pattern\n2-insert new user\n3-insert list of users\n4-Pagination\n5-Delete\n')) 

def pattern(SQL): 
    config = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=t10o10.10")
    current = config.cursor() 
    current.execute(SQL) 
    res = current.fetchall() 
    current.close() 
    config.commit() 
         
    if len(res)!=0: 
        for row in res: 
            print(str(row[0]),end = " ")
            print(str(row[1]))
                 
    else:  
        print('Nothing found!') 
def update(SQL): 
    config = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=t10o10.10")
    current = config.cursor() 
    current.execute(SQL) 
    current.close() 
    config.commit() 

def insert(name, phonenumber): 
     
    SQL = "Select * from phone_book2 where firstname = '" + name + "';" 
    
    config = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=t10o10.10")
    current = config.cursor() 
    current.execute(SQL) 
    res = current.fetchall() 
    current.close() 
    config.commit() 
 
    if len(res) != 0: 
        SQL = "UPDATE phone_book2 SET phonenumber = '"+ phonenumber + "' WHERE firstname = '" + name +"';" 
        update(SQL) 

    else: 
        SQL = "INSERT INTO phone_book2 (firstname, phonenumber) VALUES ('" + name + "','" + phonenumber +"');"  
        current.execute(SQL) 
        current.close() 
        config.commit() 

def pagination(SQL, page): 
    SQL += " OFFSET " + str((int(page)-1) * 3)  + " ROWS FETCH NEXT 3 ROWS ONLY" 
    config = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=t10o10.10")
    current = config.cursor() 
    current.execute(SQL) 
    res = current.fetchall() 
    current.close() 
    config.commit() 
         
    if len(res)!=0: 
        for row in res: 
            print(str(row[0]), end =" ") 
            print(str(row[1])) 
                 
        else: print('Nothing found!')
        
def delete(SQL): 
    config = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=t10o10.10")
    current = config.cursor() 
    current.execute(SQL) 
    current.close() 
    config.commit() 
     
 
if function == 1: 
    b = int(input('1- Part of name     2-Part of phonenumber\n')) 
    if b == 1: 
        name = input("Write your part of name:\n") 
        SQL = "SELECT * FROM phone_book2 where firstname LIKE '"+ str(name) +"%';" 
    if b == 2: 
        phonenumber = input("Write your part of phonenumber:\n") 
        SQL = "SELECT * FROM phone_book2 where phonenumber LIKE '"+ str(phonenumber) +"%';" 
    pattern(SQL)

if function == 2: 
    name = input('Write your name:   ') 
    phonenumber = input('Write your phonenumber:   ') 
    x = re.search('^[0123456789]{11}$', phonenumber) 
    if x: 
        insert(name,phonenumber) 
 
    else:  
        print("\033[31m {}" .format('phonenumber must include 11 digits!') ) 
        print("\033[0m", end='') 
 
if function == 3: 
    with open('table2.csv') as f: 
        r = csv.reader(f)  
        for i in r: 
            name = str(i[0]) 
            phonenumber = str(i[1]) 
            print(len(phonenumber))
            if len(phonenumber) != 11:
                print('phonenumber must include 11 digits!')
            else:
                insert(name,phonenumber) 
 
if function == 4: 
    b = int(input('1-Sort by first name     2-Sort by phonenumber     3-Sort by surname\n')) 
    if b == 1: 
        SQL = 'Select * from phone_book2 order by firstname ASC' 
    if b == 2: 
        SQL = 'Select * from phone_book2 order by phonenumber ASC' 
    if b == 3: 
        SQL = '' 
    
    page = input('Write the page number: \n') 
    pagination(SQL, page) 

if function == 5: 
    b = int(input('1-Delete by name     2-Delete by phonenumber \n')) 
    if b == 1: 
        name = input('Write your name:     ') 
        SQL = "DELETE FROM phone_book2 where name = '" + name + "';" 
    if b == 2: 
        phonenumber = input('Write your phonenumber number:     ') 
        SQL = "DELETE FROM phone_book2 where phonenumber = '" + phonenumber + "';" 
 
    delete(SQL) 