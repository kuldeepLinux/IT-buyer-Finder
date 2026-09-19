import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(matches):
    if not matches:
        print("Koi match nahi mila, email nahi bhej rahe.")
        return

    body = "<h2>Naye IT Tenders Mile</h2><ul>"
    for m in matches:
        body += f"<li><b>{m['title']}</b><br>NIT: {m['nit']}<br>Cost: {m['cost']}<br>Deadline: {m['deadline']}</li><br>"
    body += "</ul>"

    message = Mail(
        from_email=os.environ.get('NOTIFY_EMAIL'),
        to_emails=os.environ.get('NOTIFY_EMAIL'),
        subject='IT Tender Alert - Match Mila',
        html_content=body
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
        print("Email bhej diya!")
    except Exception as e:
        print(f"Email error: {e}")
