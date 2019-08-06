# Maximum Subset Sum With No Adjacent Elements
# Write a function that takes in an array of positive integers and 
# returns an integer representing the maximum sum of non-adjacent 
# elements in the array. If a sum cannot be generated, 
# the function should return 0.

# Sample input: [75, 105, 120, 75, 90, 135]
# Sample output: 330 (75, 120, 135)

array = [75, 105, 120, 75, 90, 135]

def max_subset_sum_no_adjacent(array):
    '''O(n) time | O(n) space where n is the lenght 
    of the input array'''
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    max_sums = array[:]
    max_sums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])
    return max_sums[-1]

print('for this input: [75, 105, 120, 75, 90, 135]')
print("The optimal solution is:", max_subset_sum_no_adjacent(array))