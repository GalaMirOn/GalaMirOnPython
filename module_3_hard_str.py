def calculate_structure_sum(*args):
    result = 0
    lishnee = ("[", "]", "{","}","(",")",":", " ")
    apostrof = ("'", '"')
    stroka1 = str(args)
    for simvol in lishnee:
        stroka1 = stroka1.replace(simvol, '')

    for kav in apostrof:
        while stroka1.find(kav) > 0:
            nachalo = stroka1.find(kav)
            chast1 = stroka1[0:nachalo]
            chast2 = stroka1[nachalo+1:]
            konec = chast2.index(kav)
            chast2 = chast2[konec + 1:]
            text = stroka1[nachalo+1:nachalo+1+konec]
            result += len(text)
            stroka1 = chast1 + chast2

    while stroka1.find(",,") > 0:
        stroka1 +=','
        stroka1 = stroka1.replace(',,', ',')
    kav = ','
    while stroka1.find(kav) > 0:
        nachalo = stroka1.find(kav)
        text = stroka1[0:nachalo]
        result += int(text)
        stroka1 = stroka1[nachalo + 1:]

    return result


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
