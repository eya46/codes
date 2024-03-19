from math import gcd, factorial

num = int(input())

print(gcd(num * (num + 1) // 2, factorial(num)))
