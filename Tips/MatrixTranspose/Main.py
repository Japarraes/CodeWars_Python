from re import A
from matrixTranspose import *

# Transpose a matrix without using the function numpy.transpose()
    # A = [[5,4,3] --> [[5,2,4,8]]
    #     [2,4,6]  -->  [4,4,7,1]
    #     [4,7,9]  -->  [3,6,9,3]
    #     [8,1,3]]

def main():

    A = [[5,4,3],
        [2,4,6],
        [4,7,9],
        [8,1,3]]

    print(transposeMatrix(A))

if __name__ == "__main__":
    main()
