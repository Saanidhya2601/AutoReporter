import os
from dotenv import load_dotenv

# This automatically finds your .env file and loads the variables
load_dotenv()

class Config:
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
    
    # Converts the comma-separated string into a real Python list
    raw_recipients = os.getenv("REPORT_RECIPIENTS", "")
    REPORT_RECIPIENTS = [email.strip() for email in raw_recipients.split(",") if email.strip()]

    @classmethod
    def validate(cls):
        """A quick sanity check to ensure we don't run without credentials."""
        if not cls.SENDER_EMAIL:
            print("WARNING: Missing SENDER_EMAIL in .env file.")

# Run the check when the module loads
Config.validate()