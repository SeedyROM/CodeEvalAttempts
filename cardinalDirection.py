import sys
import math

test_cases = open('test.txt', 'r')

def sign(n):
	if n > 0:
		return 1
	elif n == 0:
		return 0
	elif n < 0:
		return -1

def cardinalDirection(points):
	points = points.rstrip('\n').split()
	points = map(int, points)
	currentPoint = points[0], points[1]
	destination = points[2], points[3]

	horizontal = sign(destination[0]-currentPoint[0])
	vertical = sign(destination[1] - currentPoint[1])

	#directionAngle = math.atan2(destination[0]-currentPoint[0], destination[1] - currentPoint[1])
	#directionAngle = math.degrees(directionAngle)

	cardinal = ''

	if vertical == 1:
		cardinal += 'N'
	elif vertical == -1:
		cardinal += 'S'

	if horizontal == 1:
		cardinal += 'E'
	elif horizontal == -1:
		cardinal += 'W'

	if vertical == 0 and horizontal == 0:
		cardinal = 'here'

	if cardinal:
		print cardinal



for test in test_cases:
    cardinalDirection(test)

test_cases.close()