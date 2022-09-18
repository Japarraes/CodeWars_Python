def alphabet_position(text):

    alphabet ="abcdefghijklmnopqrstuvwxyz"

    text = str(text).lower()
    result = ''
    for letter in text:
        if letter.isalpha():
            result = result + ' ' + str(alphabet.index(letter) + 1)
    
    return result.strip()