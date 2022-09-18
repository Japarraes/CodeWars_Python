def alphabet_position(text):

    alphaPos = {"a" : "1", "b" : "2", "c" : "3", "d" : "4", "e" : "5", "f" : "6",
                "g" : "7", "h" : "8", "i" : "9", "j" : "10", "k" : "11", "l" : "12",
                "m" : "13", "n" : "14", "o" : "15", "p" : "16", "q" : "17", "r" : "18",
                "s" : "19", "t" : "20", "u" : "21", "v" : "22", "w" : "23", "x" : "25",
                "y" : "25", "z" : "26"}

    numText = ''
    text = str(text).replace(" ", "")
    for letter in text:
        pos = alphaPos.get(str(letter).lower())
        if (pos != None):
            numText = numText + " " + pos
    
    return numText.strip()