def all_variants(text):
    i = 1
    while i <= len(text):
        k = 0
        while k +i <= len(text):
            _str = text[k : k + i]
            yield _str
            k += 1
        i += 1

a = all_variants("abc")
for i in a:
    print(i, end = ' ')
print()
