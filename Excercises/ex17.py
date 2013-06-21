from sys import argv
#exists module returns TRUE if file exists, FALSE if it doesn't
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?

indata = open(from_file).read()

# print "Printing %s..." % from_file
# print indata
#print "The input file is %d bytes long" % len(indata)
#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."

#raw_input()

open(to_file, 'w').write(indata) 

print "Alright, all done."

#close to free up memory space
open(to_file).close()
open(from_file).close()

