import pyodbc

server = 'database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com,1433'
database = 'VetAppointmentSystem'
username = ''
password = ''

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
