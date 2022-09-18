from Divisors import *

# Create a function named divisors/Divisors that takes an integer n > 1 and returns 
# an array with all of the integer's divisors(except for 1 and the number itself), 
# from smallest to largest. If the number is prime return the string '(integer) 
# is prime'.
# Example:
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

def main():

    print(divisors(15))  # [3,5]
    print(divisors(253)) # [11,23]
    print(divisors(24))  # [2,3,4,6,8,12]
    print(divisors(25))  # [5])
    print(divisors(13))  # "13 is prime"
    print(divisors(3))   # "3 is prime"
    print(divisors(29))  # "29 is prime"


if __name__ == "__main__":
    main()
