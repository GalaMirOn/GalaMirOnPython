def count_calls():
    global calls
    calls += 1


def string_info(str1):
    count_calls()
    kort = (len(str1),str1.upper(),str1.lower())
    return kort

def is_contains(str2,search):
    count_calls()
    vhod = str2 in search
    return vhod

calls = 0
vybor = 1
while vybor != 0:
    vybor = int(input('Введите номер функции: 1 - создание кортежа, 2 - проверка подстроки, 0 - выход: '))
    if vybor == 1:
        string = input('Введите строку: ')
        print(string_info(string))
    elif vybor == 2:
        stroka = input('Введите строку поиска: ')
        string = stroka.lower()
        list_to = (input('Введите список поиска через пробел:  '))
        list_to_s =list_to.lower()
        list_to_search = list_to_s.split(' ')
        print(is_contains(string, list_to_search))
    else:
        print(f'Функции вызывались {calls} раз(а)')
