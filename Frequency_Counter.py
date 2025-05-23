def frequency_count(string):
    arr = string.lower().split()
    set_arr = set(arr)
    for i in set_arr:
        print(f'The word {i} appears {arr.count(i)} times.')

str = 'The young man wanted a role model. He looked long and hard in his youth, but that role model never materialized. His only choice was to embrace all the people in his life he didn\'t want to be like'
frequency_count(str)