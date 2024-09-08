def deliteli(kamni):
    del_it = ''
    poisk = kamni//2+1
    for k in range(1,poisk):
        if k < kamni - k:
            del_it += str(k)+str(kamni - k)
    return del_it
proverka = {
'3 - 12',
'4 - 13',
'5 - 1423',
'6 - 121524',
'7 - 162534',
'8 - 13172635',
'9 - 1218273645',
'10 - 141923283746',
'11 - 11029384756',
'12 - 12131511124210394857',
'13 - 112211310495867',
'14 - 1611325212343114105968',
'15 - 1214114232133124115106978',
'16 - 1317115262143531341251161079',
'17 - 11621531441351261171089',
'18 - 12151811724272163631545414513612711810',
'19 - 118217316415514613712811910',
'20 - 13141911923282183731746416515614713812911'}
kol_iter = 0
prostye_chisla = {3,5,7,11,13,17,19}
for i in range(3,21):
    rezult = ''
    if i not in prostye_chisla:
        for j in range(2,i//2+1):
            kol_iter += 1
            if i % j == 0:
                rezult += deliteli(j)
    rezult += deliteli(i)
    if str(i)+' - '+rezult in proverka:
        ok = 'ПОБЕДА!!!'
    else:
        ok = 'чет не то...'
    print(str(i) + ' - ', rezult, ok)
print('Количество итераций:', kol_iter)