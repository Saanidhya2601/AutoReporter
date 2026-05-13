import smtplib
from email.message import EmailMessage
import os
from src.config import Config

def send_email(attachment_path: str):
    """
    Constructs an email with the PDF attached and sends it 
    via the configured SMTP server.
    """
    print(f"Preparing to send {attachment_path} to stakeholders...")

    # Build the email
    msg = EmailMessage()
    msg['Subject'] = "Weekly Workforce Productivity Report"
    msg['From'] = Config.SENDER_EMAIL
    msg['To'] = ", ".join(Config.REPORT_RECIPIENTS)
    msg.set_content("Hello,\n\nPlease find the automated productivity and time-allocation report attached.\n\nBest,\nAutoReporter Bot")

    # Attach the PDF safely
    with open(attachment_path, 'rb') as f:
        pdf_data = f.read()
        pdf_name = os.path.basename(attachment_path)

    msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename=pdf_name)

    # Connect to the server and send
    try:
        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
            server.starttls() # Secure the connection
            server.login(Config.SENDER_EMAIL, Config.SENDER_PASSWORD)
            server.send_message(msg)
        print("SUCCESS: Report emailed to all recipients!")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to send email. Details: {e}")