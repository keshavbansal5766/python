f = open('chai.py')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline()) = ""

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

# for line in f:
#     print(line)
    
while True:
    line = f.readline()
    if not line: break
    print(line, end="")