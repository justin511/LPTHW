from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
#f.seek(0) rewinds the file back to the beginning
def rewind(f):
	f.seek(0)

#each time f.readline is run, it reads a new line.
#read a line from the file and moving the read head to right after the \n that ends that file.
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
