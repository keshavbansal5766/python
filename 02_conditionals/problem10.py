# 1. Recommend type of food

#1. better optimise way

species = "Monkey"
age = 6

if species == "Dog":
    if age < 2:
        food = "Puppy food"
    else:
        food = "Adult dog food"
elif species == "Cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Adult cat food"        
else:
        food = "Unknow species"

print(food)