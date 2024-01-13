import smtplib
import ssl
from email.message import EmailMessage
email_sender = 'sharmaa.v.arvinda@outlook.com'
email_password = 'Arvi@7350'
email_receivers = ['pravin.kesarkar@acc.ltd','vishal.m.singh@acc.ltd','sumesh.shetty@acc.ltd']
def send_mail(subject, body):
    try:
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = ', '.join(email_receivers)
        em['Subject'] = subject
        em.set_content(body)
        # Set up the plain text and HTML versions of the message
        em.set_content("This is a plain text email. Please enable HTML to view.")
        em.add_alternative(body, subtype='html')
        context = ssl.create_default_context()
 
        with smtplib.SMTP('smtp.outlook.com', 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(email_sender, email_password)
            smtp.send_message(em)
        print("Your email has been sent successfully!")
    except Exception as e:
        print("You email not been sent fail.",e)