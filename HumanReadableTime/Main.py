from humanReadableTimeV2 import *
# from whoLikesitV2 import *
# from whoLikesitV3 import *
# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people 
# that like an item. It must return the display text as shown in the examples:
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
#
#Note: For 4 or more names, the number in "and 2 others" simply increases.

def main():

    print(make_readable(0))         #-->"00:00:00"
    print(make_readable(5))         #-->"00:00:05"
    print(make_readable(60))        #-->"00:01:00"
    print(make_readable(86399))     #-->"23:59:59"
    print(make_readable(359999))    #-->"99:59:59"

if __name__ == "__main__":
    main()
