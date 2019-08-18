# Minimum number of coins
Given an array of positive integers representing coin denominations 
and a single non-negative integer representing a target amount of money,
implement a function that returns the smallest number of coins needed 
to make change for that target amount using the given coin denominations. 
Note that an unlimited amount of coins is at your disposal. 
If it is impossible to make change for the target amount, return -1.

Sample Input: 7,[1,5,10]
Sample Output: 3

# Run 
python3 min_num_of_coin.py

# 5 Steps of Dynamic Programming applied to Knapsack Problem

### 1 Identify the subproblems 
I build an array in range of 0 to n where the indexes are the amount of dollar and the value is the minimum combination of coin we need to make change for the amount

### 2 Guess the first choice 
Remove coins randomly 

### 3 Recursively define the value of an optimal solution
We calculate the number of combination with the coin in and out.

###  4 Compute the value of an optimal solution (recurse and memoize)
After exploring all the possible combination recursibly, the function will stop when it reach the base case.

### 5 Solve original problem by reconstructing the sub-problems 
Add up the counts for each possibility of a coin in and out.