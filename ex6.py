#%d is for integer decimal
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#%r print string with quotes
print "I said: %r." % x
#'%s' does the same thing as %r
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#prints "Isn't that joke so funny?! %r" % False
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e