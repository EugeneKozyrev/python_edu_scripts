import os
import sys
import random


# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). 
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. 
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
def create_dir(name, count):
		for dir_num in range(1, count + 1):
			new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, dir_num))
			os.mkdir(new_path)
		print(os.listdir())

def delete_dir(name, count):
		for dir_num in range(1, count + 1):
			new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, dir_num))
			os.rmdir(new_path)
		print(os.listdir())

if __name__ == '__main__':
	create_dir('dir', 9)
	delete_dir('dir', 9)



# Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
def check_list(input_list):
	if len(input_list) == 0:
		return None
	else:
		return random.choice(input_list)

if __name__ == '__main__':
	my_list = [1, 2, 3, 4]
	print(check_list(my_list))


# Создайте модуль main.py. 
# Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. 
# Вызовите каждую функцию в main.py и проверьте что все работает как надо
print('You''re in main.py' )