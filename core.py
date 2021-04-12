import os
import sys
import shutil
import datetime

def save_log(message):
	log = f'{datetime.datetime.now()} - {message}'
	with open('log.txt', 'a', encoding='utf-8') as f:
		f.write(log + '\n')

def list_dir(folders_only=False):
	if folders_only:
		print([item for item in os.listdir() if os.path.isdir(item)])
	else:
		print(os.listdir())

def create_file(name, text=None):
	with open(name, 'w', encoding='utf-8') as f:
		if text:
			f.write(text)

def create_dir(name):
	try:
		os.mkdir(name)
	except FileExistsError:
		print('Directory is already exist')

def remove_f(name, folders_only=False):
	if folders_only:
		os.rmdir(name)
	else:
		os.remove(name)
	
def copy_f(name, new_name):
	if os.path.isdir(name):
		try:
			shutil.copytree(name, new_name)
		except FileExistsError:
			print('Directory is already exist')
	else:
		shutil.copy(name, new_name)

def cange_dir(name):
	try:
		os.chdir(name)
	except FileNotFoundError:
        print('There is no such path')

if __name__ == '__main__':
	create_file('file.txt')
	create_file('file.txt', 'some text')
	create_dir('dir_1')
	list_dir()
	list_dir(True)
	remove_f('dir_1', True)
	remove_f('file.txt')
	create_dir('dir_1')
	create_file('file.txt')
	copy_f('dir_1', 'dir_2')
	copy_f('file.txt', 'file1.txt')
	save_log('Message')