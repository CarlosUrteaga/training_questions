def rotate_right(ar, d:int):
    """
    ar is an int's array
    d is the index were we want to rotate
    example:
    ar: 1 2 3 4 5 6
    d : 2
    result 
    3 4 5 6 1 2 
    """
    temp = []
    # main logic
    for i in range(0, len(ar)):
        # keeping the numbers/elements to moved
        if i < d: 
            temp.append(ar[i])
        # swaping
        else:
            ar[i-d] = ar[i]
    # adding first elements.     
    # ar + temp
    for i in range (0, d):
        ar.append(temp[i])
    return ar

    