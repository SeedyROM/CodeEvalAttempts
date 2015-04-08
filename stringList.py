import math
import random
def stringList(n, chars):
	chars = list(chars)
	output = []
	i = 0
	while i < math.pow(n, len(chars)-1):
		perm = []
		for j in range(0, len(chars)-1):
			perm += chars[j]

		output.append(perm)
		i += 1

	print output

stringList(2, 'ab')