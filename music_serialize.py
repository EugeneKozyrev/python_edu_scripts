import pickle
import json

# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:

# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, 
# вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно. 
# В файле group.json указать кодировку utf-8.
my_favourite_group = {
	'name': 'Г.М.О.',
	'tracks': ['Последний месяц осени', 'Шапито'],
	'Albums': [{'name': 'Делать панк-рок','year': 2016},
	{'name': 'Шапито','year': 2014}]}

with open('group.pickle', 'wb') as f:
	pickle.dump(my_favourite_group, f)
	print('Object has been written')

my_favourite_group_j = {
	'name': 'Г.М.О.',
	'tracks': ['Последний месяц осени', 'Шапито'],
	'Albums': [{'name': 'Делать панк-рок','year': 2016},
	{'name': 'Шапито','year': 2014}]}

with open('group.json', 'w', encoding='utf-8') as f:
	json.dump(my_favourite_group_j, f)
	print('Json has been written')