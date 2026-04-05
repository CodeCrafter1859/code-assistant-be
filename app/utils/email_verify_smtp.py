import smtplib
from email.mime.text import MIMEText
from app.config import SMTP_PORT, SMTP_SERVER, SENDER_EMAIL, APP_PASSWORD


def send_otp_email(to_email, otp):
    subject = "Your OTP Verification Code"
    body = f"Your OTP is: {otp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()