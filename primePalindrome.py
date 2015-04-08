import math
from collections import deque

def isPrime(n):
	if n % 2 == 0 and n > 2: 
		return False
	return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def primePalindrome():
	highest = 0
	for i in range(1000):
		if isPrime(i):
			palindrome = False
			n = deque(list(str(i)))
			while len(n) > 1:
				if n.pop() == n.popleft():
					palindrome = True
				else:
					palindrome = False
			if palindrome: highest = i
	print highest

primePalindrome()