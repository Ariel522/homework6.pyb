#Работа со словарями
my_dict = {'kirill': 2002, 'kola' : 1999, 'vlad' :2005}
print(my_dict)
print(my_dict['kirill'])
print(my_dict.get('kamila'))
my_dict.update({'sveta' : 2040, 'roman' : 2000} )
print(my_dict)
my_dict.pop('kola')
print(my_dict)

#Работа с множествами
my_set = {32, 'kivi', 1900, 24.2, 32, 1900, 'kivi'}
print(my_set)
my_set .add(5)
my_set .add('cool')
my_set .discard('kivi')
print(my_set)






