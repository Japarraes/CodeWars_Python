def generate_hashtag(s):

    hashtag = "#"
        
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(hashtag) > 140) else hashtag