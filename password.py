password = input("Enter your password: ")
 

spec = None
upper = None
lower = None
digit = None 
for char in password:
    if not char.isalnum():
        spec = True
    if char.isupper():
        upper = True
    if char.islower():
        lower = True
    if char.isdigit():
        digit = True
if spec and upper and lower and digit:
    print("Strong password")
else:
    print("Weak password")

