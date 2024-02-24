from email.message import EmailMessage
import smtplib
def Send_Alert(subject):
    sender = "PVEWOffical@outlook.com"
    recipient = "akuforiji@pvamu.edu"
    message = "This is an Alert. We Suspect that your current surrounding are no longer safe, evacuation recommended"

    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(message)

    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=25)
    smtp.starttls()
    smtp.login(sender, "Burner.Lord123")
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit() 