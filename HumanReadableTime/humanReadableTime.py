def make_readable(seconds):

    h = '00'
    min = '00'
    sec = '00'

    if (seconds < 60):

        sec = str(seconds).zfill(2)

    else:

        minuts = seconds / 60
        
        if (minuts < 60):
            
            min = str(int(minuts)).zfill(2)
            sec = str(int(seconds % 60)).zfill(2)

        else:

            h = str(int(minuts / 60)).zfill(2)
            min = str(int(minuts % 60)).zfill(2)
            sec = str(int(seconds % 60)).zfill(2)

    return (f"{h}:{min}:{sec}")
