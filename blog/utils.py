from django.core.mail import send_mail
from dotenv import load_dotenv
import os
from django.conf import settings

load_dotenv()

def send_mail_to_admin(object):
    subject = '100 просмотров'
    message = f'''Поздравляю, у вас 100 просмотров на статье: "{object.title}"
    \nПерейти к статье: http://127.0.0.1:8000/blog/article/{object.slug}
    '''

    email_user = settings.EMAIL_HOST_USER
    recipient_list = [email_user]
    print(2)
    send_mail(subject, message, email_user, recipient_list, fail_silently=False)
    print(3)