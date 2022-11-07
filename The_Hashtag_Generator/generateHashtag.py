def generate_hashtag(s):

    if (s == ""):
        return False
    
    # Capitalize every word
    hashtag = "#" + s.title().replace(" ", "")

    if (len(s)) > 140:
        return False
    
    return hashtag