dict = {}
while True:
    action = input("Enter s to store in gradebook. Enter q to query from gradebook")

    
    if action == 's':
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        dict[name] = marks

    if action == 'q':
        name = input("Enter name: ")
        print(dict[name])
