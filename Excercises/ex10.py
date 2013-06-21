tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# print "\\" #Backslash()
# print "\'" #Single Quote '
# print "\"" #Double Quote "
# print '\a' #ASCII Bell
# print '\b' #ASCII Backspace
# print '\f' #ASCII Formfeed
# print '\n' #ASCII Linefeed
# print '\N{name}' #Character named name in the Unicode database
# print '\r ASCII' #Carriage Return
# print '\t ASCII' #Horizontal Tab
# print '\uxxxx' #Character with 16-bit hex value xxxx
# print "\Uxxxxxxxx" #Character with 32-bit hex value xxxxxxxx
# print '\v' #ASCII Vertical Tab
# print '\ooo' #Character with octal value ooo
# print '\xhh' #Character with hex value hh

		
while True:
	for i in ['/','-','\\','|']:
		print '%s\r' % i,
		

