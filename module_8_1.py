def add_everything_up(a, b):
    try:
        sum = a + b
    except TypeError as exp:
        # print('Не мешайте кашу с мухами! Ладно, одну муху можете выкинуть из каши!')
        print('Ошибка сложения строки и числа:', exp)
        if type(a) != 'str':
            a = str(a)
        if type(b) != 'str':
            b = str(b)
            sum = a + b
    finally:
        return sum

print(add_everything_up(123.457, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.457, 7))