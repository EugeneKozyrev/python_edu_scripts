from core import save_log, list_dir, create_file, create_dir, remove_f, copy_f, cange_dir
import sys

try:
	command = sys.argv[1]
except IndexError:
	print('missing required parameter')
try:
	print('write "help" for displaying hints')
	save_log('Start')
	if command == 'list':
	list_dir()
	elif command == 'file':
	try:
		first_param = sys.argv[2]
		second_param = sys.argv[3]
	except IndexError:
		print('missing required parameter')
	else:
		create_file(first_param, second_param)
	elif command == 'dir':
	try:
		first_param = sys.argv[2]
	except IndexError:
		print('missing required parameter')
	else:
		create_dir(first_param)
	elif command == 'rem':
	try:
		first_param = sys.argv[2]
		second_param = sys.argv[3]
	except IndexError:
		print('missing required parameter')
	else:
		remove_f(first_param, second_param)	
	elif command == 'cop':
	try:
		first_param = sys.argv[2]
		second_param = sys.argv[3]
	except IndexError:
		print('missing required parameter')
	else:
		copy_f(first_param, second_param)
	elif command == 'help':
	print('command "list" - outputs all files from the current directory')
	print('command "file" - creates a file, the first parameter takes the name of the file, the second the text written to this file')
	print('command "dir" - creates a bundled directory')
	print('command "rem" - deletes the file, if you specify the second parameter as True, deletes the director')
	print('command "cop" - copies a file or directory')
	elif command == 'change':
	try:
		first_param = sys.argv[2]
	except IndexError:
		print('missing required parameter')
	else:
		cange_dir(first_param)
	save_log('Finish')
except NameError:
	print(Enter the command) 