import numpy as np
import matplotlib.pyplot as plt 
import mysql.connector
import os
connection = mysql.connector.connect(
    host="db",
    user="root",
    password="root"
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS company_db;")
cursor.execute("USE company_db;")
file_path = "file"
if os.path.exists(file_path):
    print("Path Exist")
    with open(file_path,"r") as file:
        data = file.read()
        print("File Read Successfully")
    
    

#for checking the data in tables.
cursor.execute("Insert into Emp(employee_id, EmpName, Salary) values (1,'Ahmad',5000);")
print("Data Inserted Successfully")
cursor.execute("select EmpName from Emp;")
records = cursor.fetchall()
print("Employee Table Records")
for record in records:
    print(record)
