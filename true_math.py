def divide(first, second):
    from math import inf

    if second == 0:
        print('Бесконечность!')
        rez = inf
    else:
        rez = first / second
    return rez