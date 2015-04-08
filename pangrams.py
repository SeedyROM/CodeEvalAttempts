def pangrams(s):
	s = [x for (x.rstrip()) in s]
	print s

pangrams('A slow yellow fox crawls under the proactive dog')