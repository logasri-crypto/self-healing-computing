import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    sender = "arumugamlogasri@gmail.com"
    password = "vpzrzijaqkfrewkf"
    
    receiver = "arumugamlogasri@gmail.com" \
    "" \
    ""
    msg = MIMEText(message)
    msg["Subject"] = "Self-Healing Computing Alert"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()

        print("Alert Email Sent Successfully!")

    except Exception as e:
        print("Email Error:", e)
