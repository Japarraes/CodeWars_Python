def make_readable(seconds):

    hours = int(seconds/3600)
    min = int((seconds%3600)/60)
    sec = int(seconds%60)
    return "{:02d}:{:02d}:{:02d}".format(hours,min,sec)
