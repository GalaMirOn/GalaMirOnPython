def print_params(a=1, b='строка', c=True):
    print(a, b, c)


def print_params2(**kwargs):
    for key, value in kwargs.items():
        print(key, value, end='  ')


values_list = [7, '8KL', 78.9]
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
values_dict = {'b': 5.6, 'a': 89, 'c': 'utro'}
dict_ = {'c': 1, 'b': 2, 'a': 3}
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(values_list)
print_params(*values_list)
print_params(*values_list_2, 42)
print_params(**values_dict)
print_params2(**dict_)
