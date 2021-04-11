import pickle
import json

# Создать модуль music_deserialize.py. 
# В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию. 
# И получить объект: словарь из предыдущего задания.

with open('group.pickle', 'rb') as f:
	my_favourite_group_obj = pickle.load(f)
	print('Object has been read')
print(my_favourite_group_obj)

with open('group.json', 'r', encoding='utf-8') as f:
	json_my_favourite_group = json.load(f)
	print('Json has been read')
print(json_my_favourite_group)