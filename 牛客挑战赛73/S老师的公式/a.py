"""
S 老师丢给你了一个简单的数学问题：

n 1~10**6

求 gcd(n的累加,n的阶乘)

请你求出答案。
"""
"""
4047 False 8191128
4048 False 2024
4049 True 8199225
4050 False 2025
4051 True 8207326
4052 False 8211378
4053 False 8215431
4054 False 8219485
4055 False 8223540
4056 False 2028
4057 True 8231653
4058 False 8235711
4059 False 8239770
"""

num = int(input())


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if isPrime(num + 1):
    print(num // 2)
else:
    print(num * (num + 1) // 2)
