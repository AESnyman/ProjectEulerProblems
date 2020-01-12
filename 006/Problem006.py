# The sum of the squares of the first ten natural numbers is,

# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


upper = 100

sum_square = 0
square_sum = 0
for i in range(1, upper+1):
    sum_square += i
    square_sum += (i**2)

sum_square = sum_square**2

print("Difference: ", sum_square - square_sum)

