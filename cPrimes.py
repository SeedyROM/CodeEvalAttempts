import sys
import numpy
import math
from itertools import permutations

def isPrime(n):
	if n % 2 == 0 and n > 2: 
		return False
	return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def isUnique(a0, a1):

	u = False
	for i in range(len(a0)):
		a0 = list(numpy.roll(a0, i))
		if not a0 == a1:
			u = True
		else:
			u = False
			break
		#print a0, a1, u
	return u

def cPrimes(n):
	n = int(n.rstrip()); nRange = range(1, n+1)

	if n < 2 or n > 18:
		return

	if n == 2:
		print 1
	elif n > 2:

		d = 0

		for p in list(set(permutations(nRange))):
			test = list(p)
			#print test
			gah = False
			if isUnique(nRange, test):
				for i in range(len(test)):
					f = (i+1) % len(test)
					c = i
					comp0 = isPrime(test[c] + test[f])
					print test[c] + test[f]
					#comp1 = isPrime(test[c] + test[f])
					if comp0:
						gah = True
						d += 1
					else:
						gah = False
						break
		if gah:
			print d

	#print isUnique(nRange, [1,3,4,2])

cPrimes('4')