# Notification Service (Python)

Contains Python scripts to send notifications through a variety of media, like email and SMS. For instructional purposes.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip
  + Git

## Installation

Fork the repository from [GitHub source](https://github.com/prof-rossetti/notification-service-py).

Then clone your fork to download it onto your local computer and automatically associate it with a remote address named "origin":

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

Copy the ".env.example" file to a new file called ".env", and update the environment variables inside as necessary (see below).

### Email

For email capabilities, [sign up for a SendGrid account](https://signup.sendgrid.com/), click the link in a confirmation email to verify your account, then [create a new API key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions. Note the email address you used, and the value of the API Key, and store them in environment variables called `SENDGRID_API_KEY` and `MY_EMAIL_ADDRESS`, respectively.

## Usage

### Send Email

Send email to the address specified:

```sh
python app/send_email.py
```

## [License](/LICENSE.md)
