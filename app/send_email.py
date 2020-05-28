
# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md

import os
import pprint

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

# AUTHENTICATE

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))

# COMPILE REQUEST PARAMETERS (PREPARE THE EMAIL)

subject = "Example Notification"
content = "Hello, \n\nThis is a message from your personal notification service.\n\nCustomize this example notification content to make it useful for you! Maybe weather info? Maybe stock prices? Let your creativity guide you!"
message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=subject, html_content=content)
print("MESSAGE:", type(message))

# ISSUE REQUEST (SEND EMAIL)

try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e)
