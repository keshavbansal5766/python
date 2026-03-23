# 1. password checker

#1. better optimise way

password = "aada"
password_length = len(password)

if password_length < 6:
    strength = "Weak" 
elif password_length <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print(strength)