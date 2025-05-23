num_words = 0
num_lines = 0
num_char = 0
arr = []
with open("test.txt","r") as file:
    for line in file:
        num_lines += 1
        for char in line:
            if (char != " "):
                num_char += 1
        arr2 = line.split()
        for i in arr2:
            num_words += 1

print(f'Lines: {num_lines}, Words: {num_words}, Characaters: {num_char}')