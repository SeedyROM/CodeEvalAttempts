import sys
def mixedContent(s):
	s = s.rstrip().split(',')
	numbers = []
	words = []
	for e in s:
		if e.isdigit():
			numbers.append(e)
		elif type(e) == str:
			words.append(e)

	if len(words) > 0:
		sys.stdout.write(','.join(words))

	if len(words) > 0 and len(numbers) > 0:
		sys.stdout.write('|')
	else:
		print ''

	if len(numbers) > 0:
		sys.stdout.write(','.join(numbers) + "\n")


s = 'melon,apricot,peach,pineapple'
mixedContent(s)