'''
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

Example 1:

Input: nums = [2,3,3,2,2,4,2,3,4]
Output: 4
Explanation: We can apply the following operations to make the array empty:
- Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
- Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
- Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
- Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
It can be shown that we cannot make the array empty in less than 4 operations.
Example 2:

Input: nums = [2,1,2,2,3,3]
Output: -1
Explanation: It is impossible to empty the array.

'''

# first task is to make a dictionary with the count of the items in the array
# see if there are two identical items
# see if there are three identical items

list = [2,2,2,3,3,4,4,4,4,7,7,7]

def min_number(list):
    dictionary = {}
    print("original list:")
    print(list)
    for value in list:
        if value in dictionary:
            temp_count = dictionary[value]
            temp_count += 1
            dictionary[value] = temp_count
        else:
            dictionary[value] = 1
    # first check--look for pairs and count them        
    firstCheck = []
    secondCheck = []
    for key,value in dictionary.items():
        if value > 1 and value % 2 == 0:
            # lets handle if there are more than one pair
            times = int(value/2) # this counts the pairs
            for i in range(0,times):
                firstCheck.append(key)
        # check to see if there are groups of three?        
        second_value = value/3 # is the second value a three?
        second_count = int(second_value)
        if second_value.is_integer() == True:
            for i in range(0,second_count):
                secondCheck.append(key)

    # array firstCheck is how many pairs exist        
    print("first check")
    print(firstCheck)
    print("second check")
    print(secondCheck)
    # now test this on the array
    first_operations = len(firstCheck)
    second_operations = len(secondCheck)
    
    arraycheck = (first_operations * 2) + (second_operations * 3)
    if arraycheck == len(list):
        return first_operations + second_operations
    else:
        return -1


print(min_number(list))
