
import os
import math
import random

butter = bytearray(os.urandom(1000))

def lerp(v0, v1, t):
	return v0 + (v1-v0) * t

scale = 6

lastX = 0
for i in butter:
	x = int(math.pow(i, i/((i/2)+1))) % ((i % 25)+1)
	r = 1 if (int(random.randint(0, 1)) == 1) else -1
	x = round(lerp(x, lastX, 0.8)  * (r) * scale, 1)
	print x
	lastX = x