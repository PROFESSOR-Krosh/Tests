import sys

with open(sys.argv[1], 'r') as f1:
	xyR = f1.read()
x, y, R = [float(n) for n in xyR.split()]
with open(sys.argv[2], 'r') as f2:
	xnyn = f2.read()
xy = [float(n) for n in xnyn.split()]
for i in range(int(len(xy) / 2)):
	result = (xy[2 * i] - x)**2 + (xy[2 * i + 1] - y)**2
	if result < R**2:
		print(i, " - point in circle")
	if result == R**2:
		print(i, " - point lies on circle")
	if result > R**2:
		print(i, " - point outside")