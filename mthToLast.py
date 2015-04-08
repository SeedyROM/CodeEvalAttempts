def mthToLast(inp):
	inp = inp.rstrip('').split()
	m = int(inp[len(inp)-1])-1; inp.pop();
	print inp[(len(inp)-1) - m]

mthToLast('e f g h 8')