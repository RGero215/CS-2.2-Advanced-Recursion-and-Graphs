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

print('for this input: 7,[1,5,10] the output is 3')
print(f'The optimal solution is: {min_num_of_coins_for_change(n, denoms)}')

a = 5
print('for this input: 5,[1,5,10] the output is 1')
print(f'The optimal solution is: {min_num_of_coins_for_change(a, denoms)}')

b = 15
print('for this input: 15,[1,5,10] the output is 2')
print(f'The optimal solution is: {min_num_of_coins_for_change(b, denoms)}')