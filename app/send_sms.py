
# adapted from:
# ... https://www.twilio.com/docs/libraries/python
# ... https://github.com/s2t2/birthday-wishes-py/commit/007c23f89dba5a8a87d85c6cf843c83514fc4736
# ... https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/twilio.md

import os
import pprint

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

# AUTHENTICATE

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# ISSUE REQUEST (SEND SMS)

content = "Hello, this is a message from your personal notification service. TODO: customize me!"
message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)

# PARSE RESPONSE

pp = pprint.PrettyPrinter(indent=4)

print("----------------------")
print("SMS")
print("----------------------")
print("RESPONSE: ", type(message))
print("FROM:", message.from_)
print("TO:", message.to)
print("BODY:", message.body)
print("PROPERTIES:")
pp.pprint(dict(message._properties))
