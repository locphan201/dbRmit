import mysql.connector

def connect_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456"
    )
    cursor = mydb.cursor()
    db = "USE nanasbakery;"
    cursor.execute(db)
    return mydb, cursor

def disconnect_db(mydb, cursor):
    cursor.close()
    mydb.close()
    return mydb, cursor

def check_login(account, password):
    mydb, cursor = connect_db()
    query = """SELECT cpwd FROM Customers WHERE cphone='%s'""" %account
    cursor.execute(query)
    result = cursor.fetchall()
    mydb, cursor = disconnect_db(mydb, cursor)
    if len(result) == 0:
        return False
    else:
        return result[0][0] == password
    
def check_signup_db(info):
    if info[4] != info[5]:
        return False
    
    mydb, cursor = connect_db()
    query = """SELECT cphone FROM Customers WHERE cphone='%s'""" %info[1]
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        query = """INSERT INTO Customers (cname, cphone, caddress, cemail, cpwd) VALUES (%s,%s,%s,%s,%s);"""
        val = (info[0], info[1], info[2], info[3], info[4])
        cursor.execute(query, val)
        mydb.commit()
        mydb, cursor = disconnect_db(mydb, cursor)
        return True
    else:
        mydb, cursor = disconnect_db(mydb, cursor)
        return False