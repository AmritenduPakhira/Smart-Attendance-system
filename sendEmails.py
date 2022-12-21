import mysql.connector
import smtplib
from email.message import EmailMessage

# Connect to the database
db = mysql.connector.connect(
       host="192.168.43.97",
       user="Nilanjan",
       password="itripamrit",
       database="VIZION" 
)

# Create a cursor
cursor = db.cursor()

# Execute a SQL query to extract all names from the 'students' table
cursor.execute('SELECT USERNAME FROM UserAttendance')

# Fetch the results
results = cursor.fetchall()

# Create an empty list to store the names
studentNames = []

# Iterate over the results and append each name to the list
for row in results:
    studentNames.append(row[0])

# Print the list of names
print(studentNames)

# Set the sender and recipient addresses
sender = 'amritendu4839.be21@chitkara.edu.in'
recipients = [f'{name}.be21@chitkara.edu.in' for name in studentNames]

# Create the email message
msg = EmailMessage()
msg['Subject'] = 'REGARDING ATTENDANCE'
msg['From'] = sender
msg['To'] = recipients
query = "SELECT USERNAME, Date, DateTime FROM UserAttendance"
cursor.execute(query)

# Print the selected data
for row in cursor:
    print(row[0], row[1], row[2])
msg.set_content('Hello students,\n\nThis is a test email from Raspvizion.\n\nBest regards,\nRaspvizion')

# Connect to the Gmail SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Log in to the Gmail account
server.login('amritendu4839.be21@chitkara.edu.in', 'Amrit91265627@@')

# Send the email
server.send_message(msg)

# Disconnect from the server
server.quit()

   

