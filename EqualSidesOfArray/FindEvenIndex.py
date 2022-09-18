
import numpy as np

def find_even_index(arr):
    
    sumLeft = 0
    sumRight = 0

    arr_index = []
    arr_left = np.array([])
    arr_right = np.array([])
    arr2 = np.array(arr)
    
    for i in range(0, arr2.size):
        
        arr_left = arr2.take(range(0, i))
        arr_right = arr2.take(range(i+1, arr2.size))
        sumLeft = sumVector(arr_left)
        sumRight = sumVector(arr_right)

        if (sumLeft == sumRight):
            arr_index.append(i)

    if not arr_index:
        return -1
    else:
        arr_index.sort()
        return arr_index[0]

def sumVector(vector):
    sum = 0
    for item in vector:
        sum += item
    
    return sum



