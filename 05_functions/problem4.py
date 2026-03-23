def func(*args):
    print(args)
    for i in args:
        print( i * 2)
    return sum(args)

print(func(1, 2, 3))