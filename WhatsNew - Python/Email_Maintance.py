import os
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# API KEY not working
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
def generate_code():
    return str(random.randint(10000,99999))
def send_verification_code(new_email):
    code = generate_code()
    message = Mail(
        from_email= "zderival@gmail.com",
        to_emails= new_email,
        subject= "Verification Code",
        html_content= f"Your verification code is: {code}</strong>"
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
        return code
    except Exception as e:
        print("Error sending email", e)
        return None
