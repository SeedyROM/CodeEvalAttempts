import random as rand
from itertools import permutations
import sys

def uglier(num):
	ugly = lambda x: True if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 else False
	num = [int(x) for x in list(str(num))]
	print len(list(permutations(num)))
	print 3**6


uglier(123456)