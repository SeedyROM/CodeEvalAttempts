from collections import Counter

def lowU(string):
	string = string.rstrip()
	s = string.split()
	inp = list(map(int, s))
	print string
	unique = 0
	c = Counter(inp)
	for e in inp:
		if c[e] == e:
			print c[e]-1
			break
	return unique

print lowU('3 3 9 1 6 5 8 1 5 3')