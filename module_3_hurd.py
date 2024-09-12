def counter_in_list(element):
    global rez
    # print('подпрограмма counter', element)
    for j in range(len(element)):
        if isinstance(element[j], int):
           rez += int(element[j])
        elif isinstance(element[j], str):
           rez += len(element[j])
        # print(element[j], ' rez = ', rez)


def elem_dict(dict_1):
    global rez

    for key, value in dict_1.items():
        # print(key, value, end='  ')
        if isinstance(key, int):
           rez += key
        elif isinstance(key, str):
            rez += len(key)
        if isinstance(value, int):
           rez += value
        elif isinstance(value, str):
            rez += len(value)


def calculate_structure_sum(*arg):
    global rez
    type_list = list(arg)
    # print('Рекурсия ', type(type_list), type_list)
    # print('**',type_list, 'rez = ', rez)
    # print('вход: ', type_list, 'кол-во элементов: ',len(type_list))
    if isinstance(type_list, set):
        type_list = list(type_list)
    if isinstance(type_list,list):
        # print(type_list, 'кол-во элементов: ', len(type_list), type(type_list))
        while len(type_list) == 1:
            type_list = type_list[0]
            if isinstance(type_list, set):
                type_list = list(type_list)
        kol = len(type_list)
        for i in range(0, kol):
            element = type_list[i]
            # print(i,'-й ', element, type(element))
            if isinstance(element, list) and (isinstance(element[0], int) or isinstance(element[0], str)):
                counter_in_list(element)
            elif isinstance(element, str):
                rez += len(element)
            elif isinstance(element, int):
                rez += element
            elif isinstance(element, dict):
                elem_dict(element)
            else:
                calculate_structure_sum(element)
    # print('конец цикла')
    return rez


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

rez = 0
print(calculate_structure_sum(data_structure))

