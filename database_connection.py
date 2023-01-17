import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",password="",database="Python")
test_cursor = connection.cursor()

insert_query1 = "INSERT INTO RegForm VALUES(%s,%s)"
values = ("test","test@123")

test_cursor.execute(insert_query1,values)
connection.commit()

select_query1 = "SELECT * FROM RegForm"
test_cursor.execute(select_query1)
result1 = test_cursor.fetchall()
for values in result1:
    print(values)
