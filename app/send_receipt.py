
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
EMAIL = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

SUBJ = "Sending with Twilio SendGrid is Fun"
content = "<strong>and easy to do anywhere, even with Python</strong>"

message = Mail(from_email=EMAIL, to_emails=EMAIL, subject=SUBJ, html_content=content)

try:
    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print("OOPS", e.message)
