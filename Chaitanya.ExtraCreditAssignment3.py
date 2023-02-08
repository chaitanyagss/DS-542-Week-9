import math

c = []

def smallest_multiple(a,b):
    for i in range(a,b):
        while b + 1 > a:
            c.append(a)
            a += 1
    print(math.lcm(*c))

smallest_multiple(1,20)