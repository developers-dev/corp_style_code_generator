# @dn- Notification Module

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class DNNotification:
    """
    This class is responsible for the notification service of the Danal application.
    It provides methods to send email and SMS notifications.
    """
    def __init__(self, email_host: str, email_port: int, email_user: str, email_password: str, sms_key: str):
        self.dn_email_host = email_host
        self.dn_email_port = email_port
        self.dn_email_user = email_user
        self.dn_email_password = email_password
        self.dn_sms_key = sms_key  # This is an API key for the SMS service

    def dn_send_email(self, recipient: str, subject: str, message: str) -> bool:
        """
        This function sends an email to a specified recipient.
        It returns True if the email was sent successfully, otherwise it returns False.
        """
        msg = MIMEMultipart()
        msg["From"] = self.dn_email_user
        msg["To"] = recipient
        msg["Subject"] = subject
        body = MIMEText(message, "plain")
        msg.attach(body)

        try:
            server = smtplib.SMTP(self.dn_email_host, self.dn_email_port)
            server.starttls()
            server.login(self.dn_email_user, self.dn_email_password)
            text = msg.as_string()
            server.sendmail(self.dn_email_user, recipient, text)
            server.quit()
            return True
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
            return False

    def dn_send_sms(self, recipient: str, message: str) -> bool:
        """
        This function sends an SMS to a specified recipient.
        It returns True if the SMS was sent successfully, otherwise it returns False.
        """
        # This is a dummy implementation, as it's not possible to send an SMS without a proper SMS gateway
        # In a real-world application, you would use an SMS API here
        print(f"SMS to {recipient}: {message}")
        return True

def dn_main():
    """
    This is the main function that creates a Notification object and uses it to send an email and an SMS.
    """
    notification = DNNotification("smtp.gmail.com", 587, "email@gmail.com", "password", "sms_key")

    email_sent = notification.dn_send_email("recipient@gmail.com", "Hello", "This is a test email from Danal.")
    if email_sent:
        print("The email was sent successfully.")
    else:
        print("The email could not be sent.")

    sms_sent = notification.dn_send_sms("0123456789", "This is a test SMS from Danal.")
    if sms_sent:
        print("The SMS was sent successfully.")
    else:
        print("The SMS could not be sent.")

if __name__ == "__main__":
    dn_main()