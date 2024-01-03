import random


def check_input(a):
    if len(a) == 2 and isinstance(a[0], int) and isinstance(a[1], int):
        if int(a[0]) < int(a[1]):
            return True
    return False


def get_ladder(a, b):
    n = random.randint(a, b)
    c = []
    for i in range(b, n-1, -1):
        c.append(i)
    for i in range(a, n+1):
        c.append(i)
    return c


def main(c):
    for i in c:
        if check_input(i):
            a = int(i[0])
            b = int(i[1])
            c = get_ladder(a, b)
            for j in c:
                print("*"*int(j))
    return
