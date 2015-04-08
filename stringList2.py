import sys
from itertools import product
from collections import OrderedDict

def stringList(i):
	i = i.rstrip().split(',')

	length = int(i[0])
	chars = str(i[1])

	p = sorted(list(OrderedDict.fromkeys(product(chars, repeat=length))))

	p = ','.join([''.join(x) for x in p])

	if length == 1:
		print chars[0]
	else:
		print p

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    stringList(test)

test_cases.close()