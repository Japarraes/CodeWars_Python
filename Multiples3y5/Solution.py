def solution(number):
    
    sum = 0

    if (number < 0):
        return 0

    # Calculate multiples of 3 and 5 and store in a conjunto (delete duplicate automatic)
    multiplos3 = ([])
    multiplos5 = ([])
    for num in range(number):
        
        if num == 0: continue

        if num % 3 == 0:
            multiplos3.append(num)
        
        if num % 5 == 0:
            multiplos5.append(num)
    
    all_multiplos = set(multiplos3 + multiplos5)
    for item in all_multiplos:
        sum += item

    return sum