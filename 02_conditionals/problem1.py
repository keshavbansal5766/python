# 1. Tumhara question tha: Child (< 13) Teenager (13–19) Adult (20–59) Senior (60+)

#1. better optimise way to use elif
def age_category(age):
    if age < 13:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

    
print(age_category(12))
print(age_category(18))
print(age_category(25))
print(age_category(70))


# without defination
age = int(input("Please enter below age"))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")