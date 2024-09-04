my_dict = {'Vera':2005,'Nadezda':1996,'Kiril':1999,'Semjon':1991,'Svetlana':2004}
print('Dict: ',my_dict)
print('Existing value: ',my_dict['Kiril'])                                         # 1999
print(my_dict.get('Katya','Такого имени не зарегистрировано'))  # Такого имени не зарегистрировано
my_dict.update({'Alex':2001,'Viktor':2008})
print(my_dict)
del my_dict['Nadezda']
udal = my_dict.pop('Semjon')
print("Был удален 'Semjon' ",udal)
print(my_dict.items())

my_set = {1,2,3,'f','h',2,5,0,1,'a','b'}
print('Set: ',my_set)
my_set.add(6)
my_set.add('y')
my_set.discard('a')
print('Modified set: ',my_set)


