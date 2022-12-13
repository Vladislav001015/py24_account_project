from django.core.mail import send_mail
from main_app.celery import app

@app.task
def send_confirmation_email_celery(email, code):
    import time
    # time.sleep(10)
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        full_link,
        'vladislav001015@gmail.com',
        [email]
    )

@app.task
def spam_message():
    send_mail(
        'привет мы из py24',
        'как дела?',
        'vladislav001015@gmail.com',
        ['vladislav001015@gmail.com']
    )