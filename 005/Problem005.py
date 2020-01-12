# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def compute(i, upper):
	for j in range(int(upper/2), upper):
		if i%j != 0:
			return False
	return True

upper = 20
found = False
i = upper

while not found:
	found = compute(i, upper)
	i += upper

print(i-upper)