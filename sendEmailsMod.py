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

# Fetch the USERNAME, Date, and DateTime from the UserAttendance table
cursor = db.cursor()
query = "SELECT USERNAME, Date, DateTime FROM UserAttendance"
cursor.execute(query)
results = cursor.fetchall()

# Iterate over the results and send an email to each user's email address
for row in results:
    username = row[0]
    date = row[1]
    datetime = row[2]
    
    sender = "amritendu4839.be21@chitkara.edu.in"
    recipient = f"{username}.be21@chitkara.edu.in"
    subject = "Attendance Summary"
    body = f"Dear {username},\n\nYour attendance on {date} at {datetime} has been recorded.\n\nSincerely,\nVIZION ATTENDANCE SYSTEM"

    message = f"Subject: {subject}\n\n{body}"
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(sender, "Amrit91265627@@")
    smtp_obj.sendmail(sender, recipient,message)

        
smtp_obj.quit()
