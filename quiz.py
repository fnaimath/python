print("We're going to do a quiz game. Let's begin")
score = 0

print("What's 9 + 10?")
answer1 = input("A)12   B)13    C)19    D)20 ")
if answer1 == 'C':
    print("Correct!")
    score = score + 10
else:
    print("Wrong!")

print("What's the capital of New Jersey?")
answer1 = input("A)Dallas   B)Atlanta    C)Toronto    D)Trenton ")
if answer1 == 'D':
    print("Correct!")
    score = score + 10
else:
    print("Wrong!")

print("How many senators are in the US Senate?")
answer1 = input("A)50   B)100    C)25    D)10 ")
if answer1 == 'B':
    print("Correct!")
    score = score + 10
else:
    print("Wrong!")

print("Final score: ", score)
