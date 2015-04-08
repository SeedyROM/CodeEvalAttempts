import sys
test_cases = open('test.txt', 'r')

longest = []
outputLength = 0

for i, test in enumerate(test_cases):
    test = test.rstrip()
    if i == 0:
    	outputLength = int(test)
    longest.append(test)

longest.sort(key=len, reverse = True)

for i in range(outputLength):
	print longest[i]

test_cases.close()