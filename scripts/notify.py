import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(matches):
    if not matches:
        print("Koi match nahi mila, email nahi bhej rahe.")
        return

    gmail_address = os.environ.get('NOTIFY_EMAIL')
    app_password = os.environ.get('GMAIL_APP_PASSWORD')

    if not gmail_address or not app_password:
        print("Gmail credentials missing!")
        return

    body = "<h2>Naye IT Tenders Mile</h2><ul>"
    for m in matches:
        body += f"<li><b>{m['title']}</b><br>NIT: {m['nit']}<br>Cost: {m['cost']}<br>Deadline: {m['deadline']}</li><br>"
    body += "</ul>"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'IT Tender Alert - Match Mila'
    msg['From'] = gmail_address
    msg['To'] = gmail_address
    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(gmail_address, app_password)
            server.send_message(msg)
        print("Email bhej diya!")
    except Exception as e:
        print(f"Email error: {e}")
