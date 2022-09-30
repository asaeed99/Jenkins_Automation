from email.message import EmailMessage
import ssl
import smtplib
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# Required positional argument
parser.add_argument('--smtp_server_name', type=str,
                    help='A required integer positional argument')
parser.add_argument('--smtp_server_port', type=str,
                    help='A required integer positional argument')

parser.add_argument('--sender_email', type=str,
                    help='A required integer positional argument')
parser.add_argument('--sender_pass', type=str,
                    help='A required integer positional argument')
parser.add_argument('--receiver_emails', type=str,
                    help='A required integer positional argument')
parser.add_argument('--email_body', type=str,
                    help='A required integer positional argument')

args = parser.parse_args()

email_sender = args.sender_email
email_password = args.sender_pass
email_recipients = args.receiver_emails.strip().split(",")

subject = "BPI tools Maintenance!"
message = args.email_body

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_recipients
email['Subject'] = subject
email.set_content(message)

# Add SSL (layer of security)
context = ssl.create_default_context()

def main():
    # exception handling
    try:
        # Log in and send the email
        with smtplib.SMTP_SSL(args.smtp_server_name, args.smtp_server_port, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_recipients, email.as_string())
    except smtplib.SMTPException:
        raise

if __name__ == '__main__':
    main()
