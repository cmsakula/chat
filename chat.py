import os

def read_file_eric(file_name):
	lines = []
	Converted_String = ''
	chatter1 = 'Allen'
	chatter2 = 'Tom'
	chatter = ''
	if os.path.isfile(file_name):
		# read file
		with open(file_name, 'r', encoding = 'utf-8-sig') as f:
			for line in f:
				if chatter1 == line.strip(): 
					chatter = chatter1 
					continue
				elif chatter2 == line.strip(): 
					chatter = chatter2
					continue
				Converted_String = chatter + ': ' + line.strip()
				lines.append([Converted_String])   
		print(lines)
	return lines

# write chat to file
def write_file_eric(file_name, chat):
	with open(file_name, 'w', encoding='utf-8') as f: # with is used to automatically close the file without explicitly close it
		for c in chat:
			f.write(c[0] + '\n')

def read_file(file_name):
	lines =[]
	with open(file_name, 'r', encoding = 'utf-8') as f:
			for line in f:
				lines.append(line.strip())  
	return lines

def convert(lines):
	new = []
	chatter1 = 'Allen'
	chatter2 = 'Tom'
	person = None # declare as NULL
	for line in lines:
		if line == chatter1 :
			person = chatter1
			continue
		elif line == chatter2:
			person = chatter2
			continue
		if person: # if this variable has assinged value
			new.append(person + ': ' + line)
	# print(new) debug use
	return new

def write_file(file_name, lines):
	with open(file_name, 'w', encoding='utf-8') as f: # with is used to automatically close the file without explicitly close it
		for c in lines:
			f.write(c + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)  
	write_file('output.txt', lines)

main()
