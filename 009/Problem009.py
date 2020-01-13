# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def compute(n):
    a = 1
    b = 2
    c = n - a - b

    for a in range (1, int(n/2)):
        for b in range(a+1, n):
            c = n-a-b
            print(a, b, c)
            if a**2 + b**2 == c**2:        
                return a,b,c

a,b,c = compute(1000)
print(a, b, c)
print(a*b*c)
