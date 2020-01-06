# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

boundary = 1000
total = 0
i = 0
while i*3 < boundary:
    if not i*3 % 5 == 0:
        total += i*3
    i += 1
    
i = 0
while i*5 < boundary:
    total += i*5
    i += 1

print(total)