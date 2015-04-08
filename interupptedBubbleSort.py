

# So proud of my no tutorial bubblesort!!!
""" def bubbleSort(a, n):
	sorting = True
	length = len(a)
	passed = 0
	while sorting:
		nPassed = length-passed
		passed = 0
		for i in range(0, nPassed):
			v0 = int(a[i])
			v1 = int(a[i+1]) if i+1 < length else v0
			if v0 > v1:
				a[i], a[i+1] = a[i+1], a[i]
			else:
				passed += 1
		if passed == length-1:
			sorting = False
		elif passed >= int(n)-1:
			sorting = False

	return a """

import sys
def bubbleSort(a, b):
	n = len(a)
	c = 0
	while n > 0:
		newn = 0
		if n <= len(a)-int(b):
			break
		for i in range(1, n):
			if a[i-1] > a[i]:
				a[i-1], a[i] = a[i], a[i-1]
				newn = i
		n = newn
	return a


test_cases = open('test.txt', 'r')
for test in test_cases:
	test = test.split(' | ')
	test[0] = test[0].rstrip().split(' ')
	test[0] = map(int, test[0])
	test[1] = test[1].rstrip()
	print ' '.join( map(str,bubbleSort(test[0], test[1]) ) )

test_cases.close()