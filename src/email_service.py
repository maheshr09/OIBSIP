import os
import smtplib
from email.message import EmailMessage
from src.responses import speak
from src.speech import listen

# A simple mock address book to avoid the nightmare of spelling out email addresses by voice
ADDRESS_BOOK = {
    "test": "testrecipient@example.com",
    "myself": os.environ.get("EMAIL_ADDRESS", "test@example.com") 
}

def send_email_securely(recipient: str, subject: str, body: str) -> bool:
    """Handles the actual SMTP connection securely without logging passwords."""
    email_address = os.environ.get("EMAIL_ADDRESS")
    email_password = os.environ.get("EMAIL_PASSWORD")

    if not email_address or not email_password:
        speak("Email credentials are not configured in your environment variables.")
        return False

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = recipient

    try:
        # Connect to Gmail's secure SMTP server by default
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        return True
    except smtplib.SMTPAuthenticationError:
        # DO NOT print the exception object, it might echo the password
        print("SMTP Authentication Error: Invalid email or App Password.")
        speak("I could not authenticate with the email server. Please check your credentials.")
        return False
    except Exception as e:
        # Generic network or connection error
        print("SMTP Connection Error occurred.")
        speak("A network error occurred while trying to send the email.")
        return False

def handle_email():
    """Interactive conversational flow for drafting and sending an email."""
    speak("Who would you like to send the email to? You can say 'test' or 'myself'.")
    recipient_name = listen()
    
    if not recipient_name:
        speak("I didn't catch that. Cancelling email.")
        return

    # Check address book
    recipient_email = ADDRESS_BOOK.get(recipient_name.lower())
    if not recipient_email:
        speak(f"I don't have an email address for {recipient_name}. Cancelling.")
        return

    speak("What is the subject of the email?")
    subject = listen()
    if not subject:
        speak("No subject detected. Cancelling.")
        return

    speak("What is the message body?")
    body = listen()
    if not body:
        speak("No message detected. Cancelling.")
        return

    # Confirmation step
    speak(f"Okay, I will send an email to {recipient_name} with the subject '{subject}'.")
    speak("Do you want to send this now? Please say yes or no.")
    
    confirmation = listen()
    
    if confirmation and "yes" in confirmation.lower():
        speak("Sending email now...")
        success = send_email_securely(recipient_email, subject, body)
        if success:
            speak("Email sent successfully!")
    else:
        speak("Email cancelled.")
