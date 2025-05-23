
f = open("todo.txt", "x")
while True:
    select = input("Enter A if you want to add to list. Enter B if you want to remove from list. Enter C if you want to mark as complete   ")
    if select == 'A':
        add = input("Enter the task you want to add: ")
        with open("todo.txt", "a") as f:
            f.write("{add}\n")
    if select == 'B':
        number = input("Enter the line number of the task you want to delete: ")
        try:
            with open('todo.txt', 'r') as fr:
                lines = fr.readlines()
                ptr = 1
                with open('months.txt', 'w') as fw:
                    for line in lines:
                        if ptr != number:
                            fw.write(line)
                        ptr += 1
        except:
            print("error")
    if select == 'C':
        add = input("Enter the line number of the task you want to mark as complete: ")
        try:
            with open('todo.txt', 'r') as fr:
                lines = fr.readlines()
                ptr = 1
                with open('months.txt', 'w') as fw:
                    for line in lines:
                        if ptr != add:
                            fw.write(line)
                        ptr += 1
        except:
            print("error")


