def character_count(string):
    arr = []
    for char in string:
        if (char != " "):
            arr.append(char)
    set_elements = set(arr)
    for i in set_elements:
        print(f'The character {i} appears {arr.count(i)} times')

str2 = 'The young man wanted a role model. He looked long and hard in his youth, but that role model never materialized. His only choice was to embrace all the people in his life he didn\'t want to be like'
character_count(str2)