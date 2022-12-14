from django.core.mail import send_mail
from main_app.celery import app
from applications.spam.models import Spam

@app.task
def send_spam_message_to_users():
    emails = Spam.objects.all()
    send_mail(
            'привет мы из py24',
            'загляни на наш сайт http://localhost:8000/product/',
            'vladislav001015@gmail.com',
            [i.email for i in emails]
        )
    # for email in emails:
    #     send_mail(
    #         'привет мы из py24',
    #         'загляни на наш сайт http://localhost:8000/product/',
    #         'vladislav001015@gmail.com',
    #         [email.email]
    #     )