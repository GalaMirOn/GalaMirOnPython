example='Работа со строками в Python'
print(example)
print(example[0])
print(example[-1])

if len(example)//2%2==0:
    print(example[len(example)//2 - 1:])
else:
    print(example[len(example) // 2 :])

print(example[::-1])
print(example[::2])