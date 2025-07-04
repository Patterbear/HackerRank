def reverseArray(a):
    reversed_array = []
    
    for number in a:
        reversed_array.insert(0, number)
    
    return reversed_array