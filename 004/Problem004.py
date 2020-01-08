#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def reverse_number(n):
    r = 0
    print(n)
    while n > 0:
        r *= 10
        r += n % 10
        n = int(n/10)
    return r

def isPalindrome(n):
    r = reverse_number(n)
    if n == r:
        return True
    return False

palindromes = []
for i in range(999, 100, -1):
    for j in range(999 - (999-i), 100, -1):
        if isPalindrome(j*i):
            palindromes.append(i*j)
        
print(max(palindromes))
