first = "tooth"

def fNRC(string):
	string = string.rstrip()
	a = list(string)
	for i in range(len(a)):
		if string.count(a[i]) == 1:
			print a[i]
			break

fNRC(first)