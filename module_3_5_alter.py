number = input('Введите число: ')
# number = '40203'
# number = '00011101023000'
number_0 = number.replace('0','')
result = int(number_0[0])
for i in range(1,len(number_0)):
    result *= int(number_0[i])
print(result)
