import sys
import collections

test_cases = open('test.txt', 'r')
board = collections.deque(maxlen = 255*255)
for test in test_cases:
   	exp = test.rstrip().split()
   	function = exp[0]
   	if function == 'SetCol':
   		arg1 = int(exp[1])
   		arg2 = int(exp[2])

   		for i in range(0, 255):

   	elif function == 'SetRow':
   		#set row
   	elif function == 'QueryCol':
   		# query col
   	elif function == 'QueryRow':
   		#query row