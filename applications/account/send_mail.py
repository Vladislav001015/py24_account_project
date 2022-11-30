from django.core.mail import send_mail

def send_hello(email):
    send_mail(
        'Вас приветствует крутой сайт', # title
        'привет как дела?', # body
        'vladislav001015@gmail.com', # from
        [email] # to
    )