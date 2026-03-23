# yield generator function

def even(limit):
    for i in range(2, limit + 1, 2):
        yield i
        
for num in even(10):
    print(num) 
    
# def even(limit):
#     li = []
#     for i in range(2, limit + 1, 2):
#         li.append(i)
#     return li

# for num in even(10):
#     print(num)