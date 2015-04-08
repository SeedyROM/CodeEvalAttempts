from itertools import permutations

p = sorted(list(permutations('hat')))

p = [''.join(x) for x in p]

print ','.join(p)
