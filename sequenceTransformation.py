def secTrans(b, s):
	s = list(s)
	last = s[0]
	stack = [int(x) for x in b]
	print stack
	for x in stack:
		for c in s:
			if last != 'A' and x == 0:
				pass
			elif last != 'B' and x == 1:
				pass
			last = c

secTrans('1010', 'AAAAABBBBAAAA')