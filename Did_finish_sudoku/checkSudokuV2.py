def done_or_not(board):

    for i in range(9):
    
        # Check row
        if (len(set(board[i])) < 9):
            return "Try again!"

        # Check colum
        if (len(set(board[j][i] for j in range(9))) < 9):
            return "Try again!"
            
        # Check region
        # if ( len(set(board[i//3*3+k//3][i//3*3+k%3] for k in range(9))) < 9):
        #     return "Try again!"
        region = []
        for k in range(9):
            n = board[i//3*3+k//3][i//3*3+k%3]
            region.append(n)
        
        if len(set(region)) < 9:
            return "Try again!"
            
    return "Finished"