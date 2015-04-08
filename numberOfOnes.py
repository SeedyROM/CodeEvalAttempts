def numberOfOnes(n):
	b = "{0:b}".format(n)
	b = [int(x) for x in b]
	count = 0
	for i in b:
		if i == 1:
			count += 1
	print count

numberOfOnes(22)