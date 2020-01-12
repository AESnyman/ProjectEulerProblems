# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


def is_prime(n):

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i**2 <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True

x = 1
wanted = 10001
i = 2
while x <= wanted:
    ret = is_prime(i)
    if ret == True:
        x += 1

    i += 1
print(i-1)