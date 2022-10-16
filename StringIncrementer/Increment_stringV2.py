def increment_string(strng):

# The rstrip() method removes any trailing characters (characters at the end a string)
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
    
