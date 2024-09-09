def send_email(message, recipient, sender='university.help@gmail.com' ):
    proverka = recipient.find('@') != -1 and sender.find('@') != -1
    proverka_rec  = ( recipient[-4:] == '.com' or recipient[-4:] == '.net' or recipient[-3:] == '.ru')
    proverka_sen =   sender[-4:] == '.com' or sender[-4:] == '.net' or sender[-3:] == '.ru'
    proverka = proverka and proverka_rec and proverka_sen
    if not proverka:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
