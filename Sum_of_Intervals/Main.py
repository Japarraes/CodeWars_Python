from calculateSumIntervals import *

# Write a function called sumIntervals/sum_intervals() that accepts an 
# array of intervals, and returns the sum of all the interval lengths. 
# Overlapping intervals should only be counted once.
#
# INTERVALS:
# Intervals are represented by a pair of integers in the form of an array. 
# The first value of the interval will always be less than the second value. 
# Interval example: [1, 5] is an interval from 1 to 5. 
# The length of this interval is 4.
#
# Overlapping Intervals
# List containing overlapping intervals:
# [ [1,4],
#   [7, 10],
#   [3, 5] ]


def main():

#    print(sumIntervals([ [6, 10], [1, 2], [11, 15]])) # => 9
#    print(sumIntervals([ [1,4], [7, 10], [3, 5] ] )) # => 7
    print(sumIntervals([ [1,5], [10, 20], [1, 6], [16, 19], [5, 11] ])) # => 19
#    print(sumIntervals([ [0, 20], [-100000000, 10], [30, 40] ])) # => 100000030

if __name__ == "__main__":
    main()
