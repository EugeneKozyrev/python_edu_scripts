import sys

#Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»************************
def person_info(name, age, city):
	print('{}, {} years old, living in {}'.format(name, age, city))
	return '{}, {} years old, living in {}'.format(name, age, city)
person_info('Ivan', 21, 'LA')
# person_info(sys.argv[1], sys.argv[2], sys.argv[3])


#Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
def max_of_three(*args):
	print(max(args))
# max_of_three(sys.argv[1], sys.argv[2], sys.argv[3])
max_of_three(2, 10, 4)


# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#     name - строка полученная от пользователя,
#     health = 100,
#     damage = 50. 
### Поэкспериментируйте с значениями урона и жизней по желанию. 
### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. 
### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. Функция должна сама работать со словарями и изменять их значения.
def attack(person_1, person_2):
	print(person_1, person_2)
	person_1['health'] -= person_2['damage']
	print(person_1, person_2)

dict_person_1 = {'name': 'Leo', 'health': 100, 'damage': 50}
dict_person_2 = {'name': 'Max', 'health': 150, 'damage': 50}

attack(dict_person_1, dict_person_2)


# Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:

#     Наносит урон. Это улучшенная версия функции из задачи 3.

#     Вычисляет урон по отношению к броне.
def attack(person_1, person_2):
	print(person_1, person_2)
	person_1['health'] -= armor_damage(person_1, person_2)
	print(person_1, person_2)

def armor_damage(person_1, person_2):
	return person_2['damage'] / person_1['armor']

dict_person_1 = {'name': 'Leo', 'health': 100, 'damage': 50, 'armor': 1.2}
dict_person_2 = {'name': 'Max', 'health': 150, 'damage': 50, 'armor': 1.2}

attack(dict_person_1, dict_person_2)
