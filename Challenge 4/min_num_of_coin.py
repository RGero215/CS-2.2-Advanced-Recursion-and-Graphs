n = 7
denoms = [1,5,10]

def min_num_of_coins_for_change(n, denoms):
    '''Run time O(nd) time where d is the amount of denomination we have| O(n) space'''
    num_of_coins = [float('inf') for amount in range(n + 1)]
    num_of_coins[0] = 0
    frequency = {}
    for denom in denoms:
        frequency[denom] = 0
        # here we are checking if the sum of two coins is one less than n
        if denom in twoNumberSum(denoms, n - 1): # if the sum of denom is one less than n
            frequency[denom] += 1 # add one to each denom
            if denom == 1: # if the denom is one 
                frequency[denom] += 1 # add an extra one 
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], 1 + num_of_coins[amount - denom])
                if denom == n:
                    frequency[denom] += 1
            # check if the sum of denom and amount are equal to n
            if denom + amount == n:
                if amount in frequency:
                    frequency[denom] += 1
                    frequency[amount] += 1

    print("Coins", frequency)
    
    return num_of_coins[n] if num_of_coins[n] != float('inf') else - 1

def twoNumberSum(array, targetSum):
    '''
    this helper function is to find if the sum of two is equal to target
    '''
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []


print('for this input: 7,[1,5,10] the output is 3')
print(f'The optimal solution is: {min_num_of_coins_for_change(n, denoms)}')

a = 5
print('for this input: 5,[1,5,10] the output is 1')
print(f'The optimal solution is: {min_num_of_coins_for_change(a, denoms)}')

b = 15
print('for this input: 15,[1,5,10] the output is 2')
print(f'The optimal solution is: {min_num_of_coins_for_change(b, denoms)}')