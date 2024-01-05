
# Leet Code
# 2610. Convert an Array Into a 2D Array With Conditions

# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.

# Example 1:

# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]
# Explanation: We can create a 2D array that contains the following rows:
# - 1,3,4,2
# - 1,3
# - 1
# All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
# It can be shown that we cannot have less than 3 rows in a valid array.

arr = [1, 3, 4, 1, 2, 3, 1,4,4,4]
arr2 = [1,1,1,1,1,1,1,1]
arr3 = [1,2,3,4,5,6]

def findMatrix(arr):
    #1 add array to a dictionary with a count
    dictionary = {}
    count = 0
    # first check if the array value is in the dictionary?
    # if it is in there, then pull the count value and add one
    for element in arr:

        if element in dictionary:
            tempcount = dictionary[element]
            print("tempcount")
            print(tempcount, element)
            tempcount = tempcount + 1
            dictionary[element] = tempcount

        else:
            dictionary[element] = 1

        
         

        

    return dictionary

print(findMatrix(arr))