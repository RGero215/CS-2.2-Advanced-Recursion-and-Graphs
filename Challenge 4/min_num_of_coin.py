# Given an array of positive integers representing coin denominations 
# and a single non-negative integer representing a target amount of money,
# implement a function that returns the smallest number of coins needed 
# to make change for that target amount using the given coin denominations. 
# Note that an unlimited amount of coins is at your disposal. 
# If it is impossible to make change for the target amount, return -1.

# Sample Input: 7,[1,5,10]
# Sample Output: 3  (2 coins of 1, 1 coin of 5)

n = 7
denoms = [1,5,10]

def min_num_of_coins_for_change(n, denoms):
    '''Run time O(nd) time where d is the amount of denomination we have| O(n) space'''
    num_of_coins = [float('inf') for amount in range(n + 1)]
    num_of_coins[0] = 0
    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], 1 + num_of_coins[amount - denom])

    return num_of_coins[n] if num_of_coins[n] != float('inf') else - 1

print('for this input: 7,[1,5,10]')
print(f'The optimal solution is: {min_num_of_coins_for_change(n, denoms)}  (2 coins of 1, 1 coin of 5)')