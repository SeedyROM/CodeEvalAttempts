import sys
test_cases = open('test.txt', 'r')
for test in test_cases:
    test = test.rstrip().split('|')
    a = list(test[0])
    b = test[1].rstrip().split()
    output = []
    for i, v in enumerate(b):
    	output.append(a[int(v)-1])