test = '9 0 6 | 15 14 9'

def multList(string):
	a = string.split(' | ')
	a[0] = map(int, a[0].rstrip().split())
	a[1] = map(int, a[1].rstrip().split())

	output = []

	if len(a[0]) != len(a[1]):
		return

	for i in range(len(a[0])):
		output.append(a[0][i] * a[1][i])

	print ' '.join([str(x) for x in output])

multList(test)
