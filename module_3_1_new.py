def count_calls():
    global calls
    calls += 1


def string_info(str1):
    count_calls()
    kort = (len(str1),str1.upper(),str1.lower())
    return kort

def is_contains(str2,search):
    count_calls()
    str2 = str2.lower()
    search = search.lower()
    search = search.split(' ')
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
        list_to_search = (input('Введите список поиска через пробел:  '))
        print(is_contains(stroka, list_to_search))
    else:
        print(f'Функции вызывались {calls} раз(а)')
