def is_prime(func):
    def wrapper(*args):
        result = func(args)
        flag = True
        for i in range(2, result // 2):
            if result % i == 0:
                flag = False
                break
        if flag:
            print("Простое", end='  ')
        else:
            print("Составное", end='  ')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(*args)


result = sum_three(2, 3, 6)
print(result)
result = sum_three(2, 3, 6, 8, 1)
print(result)
