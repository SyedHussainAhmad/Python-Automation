import pandas as pd
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class BulkEmailSender:
    def __init__(self, smtp_host, smtp_port, smtp_username, smtp_password, sender_email, email_subject, email_content):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.sender_email = sender_email
        self.email_subject = email_subject
        self.email_content = email_content

    def send_email(self, recipient_name, recipient_email):
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient_email
            message['Subject'] = self.email_subject
            
            if recipient_name!="blank":
                email_content = self.email_content.replace('<name>',recipient_name)
            else:
                email_content = self.email_content.replace('<name>',"")

            message.attach(MIMEText(email_content, 'html'))

            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())

            print(f"Email sent to {recipient_name} at {recipient_email}")
        except Exception as e:
            print(f"Failed to send email to {recipient_name} at {recipient_email}: {e}")

    def send_bulk_emails(self, csv_file_path):
        df = pd.read_csv(csv_file_path)
        email = list(df.get('Email'))
        name = list(df.get('Name'))
        
        for recipient_name, recipient_email in zip(name,email):
            print(recipient_name,recipient_email,'\n')

            if "," in recipient_email:
                variables = [var.strip() for var in recipient_email.split(",")]
                for emails in variables:
                    self.send_email(recipient_name, emails)
            else:
                self.send_email(recipient_name, recipient_email)
            time.sleep(5)

def main():
    SMTP_HOST = "smtp.hostinger.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "connect@epresencebuilders.com"
    SMTP_PASSWORD = "F[Rfwe;:!LpjV1"
    SENDER_EMAIL = "connect@epresencebuilders.com"
    EMAIL_SUBJECT = "Your Path to Online Success Starts Here- You need to read this!"

    with open("D:\F Drive\Work\Programming\Python\Coding\Projects\Advanced Projects\Bulk email sender\content.txt") as f:
        EMAIL_CONTENT = f.read()

    csv_file_path = "D:\F Drive\Work\Programming\Python\Coding\Projects\Advanced Projects\Bulk email sender\data.csv"

    bulk_email_sender = BulkEmailSender(SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, SENDER_EMAIL, EMAIL_SUBJECT, EMAIL_CONTENT)
    bulk_email_sender.send_bulk_emails(csv_file_path)

if __name__ == "__main__":
    main()
