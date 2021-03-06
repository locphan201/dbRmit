import mysql.connector
import datetime

def connect_db():
    mydb = mysql.connector.connect(
        host="eu-cdbr-west-02.cleardb.net",
        user="b03249ea8f4171",
        password="4bf170a0"
    )
    cursor = mydb.cursor()
    db = "USE heroku_6424eae9f05fcc3;"
    cursor.execute(db)
    
    # mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="123456"
    # )
    # cursor = mydb.cursor()
    # db = "USE nanasbakery;"
    # cursor.execute(db)
    
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
        mydb, cursor = connect_db()
        query = """SELECT cpwd FROM Customers WHERE cemail='%s'""" %account
        cursor.execute(query)
        result = cursor.fetchall()
        mydb, cursor = disconnect_db(mydb, cursor)
        if len(result) == 0:
            return False
        else:
            return result[0][0] == password
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
        val = (info[0].capitalize(), info[1], info[2], info[3], info[4])
        cursor.execute(query, val)
        mydb.commit()
        mydb, cursor = disconnect_db(mydb, cursor)
        return True
    else:
        mydb, cursor = disconnect_db(mydb, cursor)
        return False
    
def get_user_info(account):
    mydb, cursor = connect_db()
    query = """SELECT cID, cname, cphone, caddress, cemail FROM Customers WHERE cphone='%s'""" %account
    cursor.execute(query)
    result = cursor.fetchall()
    mydb, cursor = disconnect_db(mydb, cursor)
    if len(result) == 0:
        mydb, cursor = connect_db()
        query = """SELECT cID, cname, cphone, caddress, cemail FROM Customers WHERE cemail='%s'""" %account
        cursor.execute(query)
        result = cursor.fetchall()
        mydb, cursor = disconnect_db(mydb, cursor)
    return result[0]

def get_best_seller():
    mydb, cursor = connect_db()
    query = """SELECT pname FROM products P, contains C WHERE P.pID = C.pID GROUP BY pname ORDER BY SUM(quantity) DESC LIMIT 4"""
    cursor.execute(query)
    result = cursor.fetchall()
    mydb, cursor = disconnect_db(mydb, cursor)
    return result

def get_product_infos():
    mydb, cursor = connect_db()
    query = """SELECT pname, price FROM Products"""
    cursor.execute(query)
    result = cursor.fetchall()
    mydb, cursor = disconnect_db(mydb, cursor)
    return result

def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def cart_checkout(items, customer):
    mydb, cursor = connect_db()
    date = get_current_time()
    query = """INSERT INTO Orders (cID, date, price, type) VALUES (%s, \'%s\', %s, 'INCOMPLETED')""" %(customer, date, items[1])
    cursor.execute(query)
    query = """SELECT oID FROM Orders WHERE cID = %s ORDER BY oID DESC LIMIT 1;""" %customer
    cursor.execute(query)
    oID = cursor.fetchall()[0][0]
    for item in items[0]:
        query = """SELECT pID FROM Products WHERE pname = \'%s\'""" %item[0]
        cursor.execute(query)
        pID = cursor.fetchall()[0][0]
        query = """INSERT INTO Contains (oID, pID, quantity) VALUES (%s, %s, %s)""" %(oID, pID, item[1])
        cursor.execute(query)
    mydb.commit()
    mydb, cursor = disconnect_db(mydb, cursor)
 
def get_order_info(customer):
    mydb, cursor = connect_db()
    query = """SELECT oID, date, price, type FROM Orders WHERE cID = %s ORDER BY oID DESC LIMIT 1;""" %customer
    cursor.execute(query)
    order = cursor.fetchall()
    if order == []:
        return None, None
    oID = order[0][0]
    if oID == None:
        return None, None
    query = """SELECT pname, quantity, price FROM products P, contains C WHERE P.pID = C.pID AND C.oID = %s;""" %oID
    cursor.execute(query)
    items = cursor.fetchall()
    mydb, cursor = disconnect_db(mydb, cursor)
    return order[0], items

def get_previous_orders(customer, oID):
    mydb, cursor = connect_db()
    query = """SELECT oID, date, price, type FROM Orders WHERE cID = %s AND oID < %s ORDER BY oID DESC LIMIT 1; """ %(customer, oID)
    cursor.execute(query)
    order = cursor.fetchall()
    if order == []:
        return None, None
    oID = order[0][0]
    if oID == None:
        return None, None
    query = """SELECT pname, quantity, price FROM products P, contains C WHERE P.pID = C.pID AND C.oID = %s;""" %oID
    cursor.execute(query)
    items = cursor.fetchall()
    mydb, cursor = disconnect_db(mydb, cursor)
    return order[0], items

def get_next_orders(customer, oID):
    mydb, cursor = connect_db()
    query = """SELECT oID, date, price, type FROM Orders WHERE cID = %s AND oID > %s ORDER BY oID ASC LIMIT 1; """ %(customer, oID)
    cursor.execute(query)
    order = cursor.fetchall()
    if order == []:
        return None, None
    oID = order[0][0]
    if oID == None:
        return None, None
    query = """SELECT pname, quantity, price FROM products P, contains C WHERE P.pID = C.pID AND C.oID = %s;""" %oID
    cursor.execute(query)
    items = cursor.fetchall()
    mydb, cursor = disconnect_db(mydb, cursor)
    return order[0], items 