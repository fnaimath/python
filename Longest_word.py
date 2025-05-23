def longest_word(string):
    arr = []
    r_string = ''
    length = 0
    for char in string:
        if (char != " "):
            arr.append(char)
        elif(char == " "):
            if (len(arr) > length):
                length = len(arr)
                arr.clear()
            else:
                arr.clear()
    for i in range(len(arr)):
        r_string += arr[i]
    return r_string

str = 'The big bad wolf gobbled all the chickens'
print(longest_word(str))