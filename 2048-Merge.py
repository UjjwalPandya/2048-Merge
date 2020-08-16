# Making a function to remove zeroes from a list before merging.
def remove_zero(lst):
    """
    Function to remove zeroes from a list
    """
    res = []
    for index in range(len(lst)):
        if lst[index] == 0:
            continue
        else:
            res.append(lst[index])
    return res

# Making a function to merge two nubers and form a new number twice the value of it.
def merging(lst):
    """
    Function that handels non zero lists merging
    """
    for index in range(len(lst)-1):
        if lst[index] == lst[index+1]:
            lst[index] *= 2
            lst[index+1] = 0
          
    return remove_zero(lst)

# Making a function to add zeroes at the empty spaces at the end of the list.
def add_zero(lst , length):
    """
    Function to add zeros to the end of the list
    """
    res = lst
    for index in range(length - len(lst)):
        res.append(0)
    return res

# Making a function to combine all the functions and merge the list.
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    res = remove_zero(line)    
    result = merging(res)
    result = add_zero(result , len(line))
    return result

# Testing the above code.
print(merge([4, 4, 8, 2, 0]))