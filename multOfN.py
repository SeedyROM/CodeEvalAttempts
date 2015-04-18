import sys
import math

def multOfN(_in):
	_in = map(int, _in.rstrip().split(','))
	x = _in[0]
	n = _in[1]

	if not ((n != 0) and ((n & (n - 1)) == 0)):
		return

	i = 1
	smaller = True
	while smaller:
		if n*i >= x and x-n > 0:
			smaller = False
			return n*i
		i += 1

test_cases = open('test.txt', 'r')

for test in test_cases:
    print multOfN(test)

test_cases.close()