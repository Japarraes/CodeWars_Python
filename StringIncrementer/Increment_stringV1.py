def increment_string(strng):

    list_str = list(strng)
    str_letters = ""
    str_digits = ""
    cnt = 0

    # Check if string contains numbers
    for item in reversed(list_str):
        if item.isdigit():
            cnt += 1
            str_digits = item + str_digits
        else:
            str_letters = "".join(list_str[0:-cnt])
            break
    
    # If no number, inizialice local variables with strng and zero as digit
    if (cnt == 0):
        str_letters = "".join(list_str)
        str_digits = "0"
    
    # Concatenate letters and number + 1
    strng_new = str_letters + str(int(str_digits) + 1).zfill(len(str_digits))
    
    return strng_new
    
