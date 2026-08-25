import smtplib
from email.message import EmailMessage
from src.utils.config_loader import load_config
from src.audio.speaker import speak

def handle_email():
    config = load_config()
    email_address = config.get("email_address")
    email_password = config.get("email_password")
    
    if not email_address or not email_password:
        speak("Email credentials are not configured in config.json.")
        return
    
    speak("This is a placeholder for sending an email. In a real scenario, you would prompt for recipient and body.")
    
    # Example skeleton:
    # msg = EmailMessage()
    # msg.set_content("Test message")
    # msg['Subject'] = "Test Subject"
    # msg['From'] = email_address
    # msg['To'] = "recipient@example.com"
    # try:
    #     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #         smtp.login(email_address, email_password)
    #         smtp.send_message(msg)
    #     speak("Email sent successfully.")
    # except Exception as e:
    #     speak("Failed to send email.")

