import math

def circle_stats(r):
    area = round((math.pi * r ** 2), 2)
    circumference = round((2 * math.pi * r), 2)
    return area, circumference

a, c = circle_stats(3)
print(a, c)