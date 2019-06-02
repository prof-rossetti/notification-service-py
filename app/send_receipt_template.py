
# adapted from: https://github.com/mgallea/daily-email/blob/master/app/main.py

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
SUBJ = "Your Receipt from the Green Grocery Store"

selected_products = [
    {"id":1, "name": "Product 1"},
    {"id":2, "name": "Product 2"},
    {"id":3, "name": "Product 3"},
    {"id":2, "name": "Product 2"},
    {"id":1, "name": "Product 1"},
]

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=SUBJ)
print("MESSAGE:", type(message))

message.dynamic_template_data = {
    "subject": "Other Subject",
    "body": "Hello Body",
    "products": selected_products,
    "my_message": "This is a test!"
}
message.template_id = SENDGRID_TEMPLATE_ID


#breakpoint()
try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e)
