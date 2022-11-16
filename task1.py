import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
i = 0
while i != 1:
	if i == 0:
		i = 1
		print(i, end='')
	i = (i + m - 1) % n
	if i == 0:
		i = n
	if i != 1:
		print(i, end='')