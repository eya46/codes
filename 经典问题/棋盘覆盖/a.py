from random import randint

k = 3
w = 2**k
amount = 0
data = [[0] * w for i in range(w)]

cx = randint(0, w - 1)
cy = randint(0, w - 1)
data[cx][cy] = "M"


def print_vec():
    for i in data:
        print(" ".join(str(j).ljust(k, " ") for j in i))
    print()


print_vec()


def cover(a: int, b: int, c: int, d: int, size: int):
    if size == 1:
        return
    global amount
    amount += 1
    t = amount
    s = size // 2

    if c < a + s and d < b + s:
        cover(a, b, c, d, s)
        data[a + s - 1][b + s] = t
        data[a + s][b + s - 1] = t
        data[a + s][b + s] = t
        cover(a, b + s, a + s - 1, b + s, s)
        cover(a + s, b, a + s, b + s - 1, s)
        cover(a + s, b + s, a + s, b + s, s)
    elif c < a + s and d >= b + s:
        cover(a, b + s, c, d, s)
        data[a + s - 1][b + s - 1] = t
        data[a + s][b + s - 1] = t
        data[a + s][b + s] = t
        cover(a, b, a + s - 1, b + s - 1, s)
        cover(a + s, b, a + s, b + s - 1, s)
        cover(a + s, b + s, a + s, b + s, s)
    elif c >= a + s and d < b + s:
        cover(a + s, b, c, d, s)
        data[a + s - 1][b + s - 1] = t
        data[a + s - 1][b + s] = t
        data[a + s][b + s] = t
        cover(a, b, a + s - 1, b + s - 1, s)
        cover(a, b + s, a + s - 1, b + s, s)
        cover(a + s, b + s, a + s, b + s, s)
    elif c >= a + s and d >= b + s:
        cover(a + s, b + s, c, d, s)
        data[a + s - 1][b + s - 1] = t
        data[a + s - 1][b + s] = t
        data[a + s][b + s - 1] = t
        cover(a, b, a + s - 1, b + s - 1, s)
        cover(a, b + s, a + s - 1, b + s, s)
        cover(a + s, b, a + s, b + s - 1, s)


cover(0, 0, cx, cy, w)
print_vec()
