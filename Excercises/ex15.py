# imports argument variable module from sys package
from sys import argv

# takes two inputs from the commandline
script, filename = argv

# opens file
txt = open(filename)

print "Here's your file %r:" % filename
# prints out what's in the txt file
# read the file
# read command, function or methods
print txt.read()

print "Type the filename again:"
#asks user for filename input
file_again = raw_input("> ")

#open that file
txt_again = open(file_again)

#read the file
print txt_again.read()