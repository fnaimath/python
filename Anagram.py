def anagram_checker(string1, string2):
    str_1 = string1.lower()
    str_2 = string2.lower()

    if(len(str_1) == len(str_2)):
        if(sorted(str_1) == sorted(str_2)):
            return 'Both strings are anagrams'
        else:
            return 'Not an anagram'
    else:
        return 'Not an anagram'
    
str1 = 'line'
str2 = 'nile'
print(anagram_checker(str1,str2))