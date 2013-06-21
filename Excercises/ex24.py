print "Let's practice everything."
#\' escapes ' as an end quote
#\\ prints \
#\n new line
#\t tabs
print 'You\'d need to know \'about escapes with \\ that do \n newlines and \t tabs.'

#Using triple quote - new lines automatically insert \n
#even though you can't see it
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "----------"
print poem
print "----------"
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#returns 3 numbers
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000
#return 3 numbers and store them into variables
beans, jars, crates = secret_formula(start_point)

print "With a starting point of %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#Printing string variables directly from calling function
#Print without saving variables
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
