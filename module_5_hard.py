from time import sleep


class UrTube:
    users = []
    videos = []
    current_user = None

    class User:

        def __init__(self, nickname, password, age):
            self.nickname = nickname
            self.password = hash(password)
            self.age = age
            # print('init user')

    def log_in(self, us):
        flag = True
        for chel in ur.users:
            if chel.nickname == us.nickname and chel.password == hash(us.password):
                print(' Вход ', chel.nickname)
                ur.current_user = chel
                flag = False
                break
        return flag

    def log_out(self):
        ur.current_user = None
        # print('Текущий пользователь неопределен')

    def register(self, *args):
        # print ('юзер', args, args[0])
        us = ur.User(args[0], args[1], args[2])
        if ur.log_in(us):
            flag = True
            for chel in ur.users:
                if chel.nickname == us.nickname and chel.password != hash(us.password):
                    print(f'Пользователь {us.nickname} уже существует или неверный пароль')
                    flag = False
                    ur.current_user = None
                    break
            if flag:
                ur.users.append(us)
                ur.current_user = us
                # print('Новый пользователь: ', us.nickname)
            if ur.current_user != None:
                print('Текущий пользователь: ', ur.current_user.nickname)
            else:
                ur.log_out()
                # print('Текущий пользователь неопределен')

    class Video:

        def __init__(self, title, duration, time_now=0, adult_mode=False):
            self.title = title
            self.duration = duration
            self.time_now = time_now
            self.adult_mode = adult_mode
            # print('init video', self)

    def add(self, baza, *args):
        # print(' аргументы',baza,  args)
        vid = baza
        flag = True
        for klip in ur.videos:
            if vid.title == klip.title:
                # print(f'Видео {vid.title} уже существует')
                flag = False
                break
        if flag:
            ur.videos.append(vid)
        if args != None:
            for vid in args:
                flag = True
                for klip in ur.videos:
                    if vid.title == klip.title:
                        # print(f'Видео {vid.title} уже существует')
                        flag = False
                        break
                if flag:
                    ur.videos.append(vid)

    def watch_video(self, title):
        if ur.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        flag = False
        for klip in ur.videos:
            if klip.title == title:
                if klip.adult_mode:
                    if ur.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        return
                while klip.time_now <= klip.duration:
                    print(klip.time_now, end=' : ')
                    sleep(0.1)
                    klip.time_now += 1
                flag = True
                klip.time_now = 0
                print('Конец видео')
        if not flag:
            print('Такого видео не найдено')

    def get_videos(self, poisk):
        # print(f' Поиск по строке "{poisk}" :')
        get_vid = []
        for stroka in ur.videos:
            if poisk.upper() in stroka.title.upper():
                # print('Видео: ', stroka.title)
                get_vid.append(stroka.title)
        return get_vid

    def list_videos(self, spisok):
        sp = []
        for elem in spisok:
            sp.append(elem.title)
        return sp

    def list_users(self, spisok):
        sp = []
        for elem in spisok:
            sp.append(elem.nickname)
        return sp


current_user = None
ur = UrTube()
v1 = ur.Video('Лучший язык программирования 2024 года', 200)
v2 = ur.Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = ur.Video('Сколько стоят облака?', 20)
print('Добавление видео')
ur.add(v1, v2)
print(ur.list_videos(ur.videos))
ur.add(v3)
print(ur.list_videos(ur.videos))

print('Проверка поиска')
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print('Текущий пользователь: ', current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

print(ur.list_users(ur.users))

