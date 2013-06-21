mystring = 'hello'

char_count = dict()
for char in mystring:
	count = char_count.get(char, 0 )
	print char, count
	count += 1
	char_count[char] = count
	
print char_count

example = {'a':100, 'b':200}

print example.get('c',0)


