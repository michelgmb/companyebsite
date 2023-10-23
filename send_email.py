import smtplib , ssl
import os

def send_email(message):
    global server
    port = 465  # For SSL
    host = "smtp.gmail.com"
    username = 'devopsesi2022@gmail.com'
    password = os.getenv("PASSWORD")
    receiver = 'devopsesi2022@gmail.com'
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        # TODO: Send email here
        server.message = message
        server.sendmail(username, receiver, message)


message = """\
    Subject: Hi Admin2
    
    from me
    This message is sent from Python test."""


#send_email(message)

