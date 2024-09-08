def deliteli(kamni):
    del_it = ''
    poisk = kamni//2+1
    for k in range(1,poisk):
        if k < kamni - k:
            del_it += str(k)+str(kamni - k)
    return del_it

prostye_chisla = {3,5,7,11,13,17,19}
for i in range(3,21):
    rezult = ''
    if i not in prostye_chisla:
        for j in range(2,i//2+1):
            if i % j == 0:
                rezult += deliteli(j)
    rezult += deliteli(i)
    print(str(i) + ' - ', rezult)





