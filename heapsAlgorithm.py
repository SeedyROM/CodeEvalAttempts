def permutations(a):
	def permute(o, v, n):
		if n == 1:
			return v[0]
		else:
			for i in range(n):
				permute(o, v, n-1);
				if n % 2 == 1:
					v[0], v[n-1] = v[n-1], v[0]
				else:
					v[i], v[n-1] = v[n-1], v[i]
		o.append(list(v))

	b  = []
	permute(b, list(a), len(a))
	return b


a = [1,2,3]
print permutations(range(9))