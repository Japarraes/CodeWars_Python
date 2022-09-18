def divisors(integer):
    
    num = 2
    arr_num = ([])
    
    for num in range(2, integer):

        if (integer % num == 0):
            arr_num.append(num)

    if (len(arr_num) != 0):
        return arr_num
    else:
        return (str(integer) + " is prime")
