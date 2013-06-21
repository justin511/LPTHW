#import argument variable from sys package
from sys import argv

#save two variables from the command line
script, filename = argv

print "We're going to erase %r." % filename
#CTRL-C quits program
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#Opening file
#What is the 'w' for?
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#truncate
#not necessary as opening up a file in 'w' overwrites the file
#target.truncate()
target.read()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()