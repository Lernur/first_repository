import random


def check_input(a):
    if len(a) == 2 and isinstance(a[0], int) and isinstance(a[1], int):
        if 0 < int(a[0]) and int(a[0]) < int(a[1]):
            return True
    return False


def get_ladder(c):
    a = int(c[0])
    b = int(c[1])
    n = random.randint(a, b)
    c = []
    for i in range(b, n-1, -1):
        c.append(i*"*")
    for i in range(a, n+1):
        c.append(i*"*")
    return c


def main(c):
    for i in c:
        if check_input(i):
            c = get_ladder(i)
            for j in c:
                print(j)
    return

