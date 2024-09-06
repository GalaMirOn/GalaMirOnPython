numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    else:
        is_prime = True
    for j in range(2,i-1):
        if i % j == 0:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime == True:
        primes.append(i)
print('Простые числа: ',primes)
print('Непростые числа: ',not_primes)