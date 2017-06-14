def answer(x, y):
    res = 0
    a = 1
    b = 0

    while (a <= x):
        res += a
        a += 1
    a -= 1

    while (b < y-1):
        res += (a+b)
        b += 1

    return res
