from django.core.mail import send_mail
from main_app.celery import app

@app.task
def spam_message():
    send_mail(
        'привет мы из py24',
        'как дела?',
        'vladislav001015@gmail.com',
        ['vladislav001015@gmail.com']
    )