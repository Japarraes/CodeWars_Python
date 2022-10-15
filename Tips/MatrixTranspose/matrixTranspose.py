import numpy as np

def transposeMatrix(matrix):

    m = np.array(matrix)

    # Verify that the matrix is rectangular or square
    i = 1
    while i < (len(m[0])):
        if len(m[i]) != len(m[i + 1]):
            raise ValueError("Matrix is not rectangular or square")
        i += 1

    # Create an empty matrix with transporse dimensions
    transposeResult = np.zeros((len(m[0]), len(m)))
    
    # Fill in the transpose result
    for a in range(len(m)):
        for b in range(len(m[0])):
            transposeResult[b][a] = matrix[a][b]

    return transposeResult