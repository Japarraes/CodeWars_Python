from whoLikesit import *
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

    print(likes([]))
    print(likes(['Peter']))
    print(likes(['Jacob', 'Alex']))
    print(likes(['Max', 'John', 'Mark']))
    print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
    print(likes(['Alex', 'Jacob', 'Mark', 'Max', 'Malcon']))

if __name__ == "__main__":
    main()
