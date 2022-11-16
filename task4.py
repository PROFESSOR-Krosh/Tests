a = [int(i) for i in input().split()]
a.sort()
if len(a) % 2 == 1:
	median = a[len(a) // 2]
else:
	median = (a[len(a) // 2 - 1] + a[len(a) // 2]) // 2
count = 0
for i in range(len(a)):
	count += abs(a[i] - median)
print(count)