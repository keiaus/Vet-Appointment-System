import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=;PWD=;')
cursor = connection.cursor()

cursor.execute("SELECT * FROM TEST")
row = cursor.fetchall()
while row:
    print(row[0])
    row = cursor.fetchall()