flatList= []
def flatlist(nest_list):
    for item in nest_list:
        if type(item) == list:
            flatlist(item)
        else:
            flatList.append(item)

nested_list = [1, [2, 3], [4, [5, 6]]]
flatlist(nested_list)
print(flatList)