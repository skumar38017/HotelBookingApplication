 

from django.core.mail import send_mail
from django.conf import settings


def send_forget_mail(email,token):
    subject = 'Your forgot password link'
    message = 'Hi, click on the link to reset your password http://localhost:8000/changepassword/'+token
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    print(message,email_from,recipient_list)
    send_mail(subject,message,email_from,recipient_list)
    return True