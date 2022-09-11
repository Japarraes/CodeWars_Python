def solution(number):
    
    sum = 0

    if (number < 0):
        return 0

    # Calculate multiples of 3 and 5 and store in a conjunto (delete duplicate automatic)
    for num in range(number):
        
        if (num % 3) == 0 or (num % 5) == 0:
            sum += num

    return sum