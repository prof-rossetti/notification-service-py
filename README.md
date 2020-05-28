# Notification Service (Python)

Contains Python scripts to send notifications through a variety of media, like email and SMS. For instructional purposes.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip
  + Git

## Installation

Fork the repository from [GitHub source](https://github.com/prof-rossetti/notification-service-py).

Then use GitHub Desktop or the command-line to "clone" or download your fork onto your local computer:

```sh
git clone https://github.com/YOUR_USERNAME/notification-service-py.git # this is the HTTP address, but you could alternatively use the SSH address
```

Navigate into your local repo before running any of the other commands below:

```sh
cd notification-service-py
```

## Setup

Create and activate an Anaconda virtual environment. From within the virtual environment, install package dependencies listed in the "requirements.txt" file:

```sh
pip install -r requirements.txt
```

Copy the ".env.example" file to a new file called ".env" (in your local repo, NOT your remote repo), and update the environment variables inside as necessary (see below).

### Email

For email capabilities, [sign up for a SendGrid account](https://signup.sendgrid.com/), click the link in a confirmation email to verify your account, then [create a new API key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions. Note the email address you used, and the value of the API Key, and store them in environment variables called `MY_EMAIL_ADDRESS` and `SENDGRID_API_KEY`, respectively.


### SMS

For SMS capabilities, [sign up for a Twilio account](https://www.twilio.com/try-twilio), click the link in a confirmation email to verify your account, then confirm a code sent to your phone to enable 2FA.

Then [create a new project](https://www.twilio.com/console/projects/create) with "Programmable SMS" capabilities. And from the console, view that project's Account SID and Auth Token. Update the contents of the ".env" file to specify these values as environment variables called `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`, respectively.

You'll also need to [obtain a Twilio phone number](https://www.twilio.com/console/sms/getting-started/build) to send the messages from. After doing so, update the contents of the ".env" file to specify this value (including the plus sign at the beginning) as an environment variable called `SENDER_SMS`.

Finally, set an environment variable called `RECIPIENT_SMS` to specify the recipient's phone number (including the plus sign at the beginning).

### Twitter

For tweeting capabilities, create a Twitter Account. Then while logged in to Twitter, visit the [Twitter Application Management Console](https://developer.twitter.com/en/apps) and click "Create New App" to create a new Twitter Application. You might have to first sign up for a Twitter developer account, and click the link in a confirmation email.

After creating a new application, click on the "Keys and Access Tokens" tab, and note the application's "Consumer Key" and "Consumer Secret". Scroll down and generate a new Access Token and note its "Access Token" and "Access Token Secret" values. Update the contents of the ".env" file to store these four values in the following environment variables, respectively: `TWITTER_API_KEY`, `TWITTER_API_SECRET`,  `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`.

## Usage

### Send Email

Send email to the address specified:

```sh
python app/send_email.py
```

Send email template with image to the address specified:

```sh
python app/send_receipt_template.py
```

### Send SMS

Send an SMS to the phone number specified:

```sh
python app/send_sms.py
```

### Send a Tweet

Post a message to the Twitter platform:

```sh
python app/send_tweet.py
```

## [License](/LICENSE.md)
