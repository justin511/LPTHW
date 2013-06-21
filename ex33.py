def whileLoop(x,inc):
	i = 0
	numbers = []
	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num
	
whileLoop(10,2)
	

def forLoop(x,inc):
	numbers = []
	for i in range(0,x,inc):
		print "At the top i is %d" % i
		numbers.append(i)
	print numbers	
	
forLoop(10,2)
