# Vet-Appointment-System
This system is used as a booking service for your pet(s).<br>
Before following the installation process please make sure to be connected to a MSSQL (Microsoft SQL Server) database that uses AWS (Amazon Web Services). Please refer to the following sources for assistance in doing so. <br> Installing MSSQL: `https://www.microsoft.com/en-us/sql-server/sql-server-downloads` Installing AWS RDS (Remote Desktop Services): `https://aws.amazon.com/rds/sqlserver/?nc=sn&loc=3&dn=6` Installing pyodbc drivers: `https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16`

Installation
---
<pre>
git clone https://github.com/Keiaus/Vet-Appointment-System.git<br>
cd Vet-Appointment-System<br>
pip install tk<br>
pip install tkcalendar<br>
pip install pyodbc<br>
</pre>

Connecting pyodbc to Your Server
---
Must be included in all files to work properly.

<pre>
connection = pyodbc.connect('DRIVER={SQL Server};PORT=<'Your port number'>;SERVER=<'Your URL link'>;UID=<'Your User ID'>;PWD=<'Your password'>;')```
cursor = connection.cursor()
</pre>

How it Works
--- 
After completing the installation process run the `mainmenu.py` file in your IDE.

- Unregistered users can create an account and view appointment times 
- Registered users can log in, update personal account information, add pet information, update pet information, remove pet information, view the calendar for available vet appointments, book appointments, cancel appointments, and search for specific vets based on location.
- Vets can log in, upload availability, update pet information, view daily appoinments, canceled appointments, and upload pet records.
- Admin can log in and manage vets.