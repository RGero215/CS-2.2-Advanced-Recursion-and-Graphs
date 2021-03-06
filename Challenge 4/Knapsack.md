# Knapsack Problem 
You are given an array of arrays. 
Each subarray in this array holds two integer values 
and represents an item; the first integer is the item's weight, 
and the second integer is the item's value. 
You are also given an integer representing the maximum capacity 
of a knapsack that you have. 
Your goal is to fit items in your knapsack, all the while maximizing 
their combined value. Note that the sum of the weights of the items 
that you pick cannot exceed the knapsack's capacity. 
Write a function that returns an array of the indices of each item picked. 

The items included in the knapsack for this optimal solution are
(("boot", 10, 60),("tent", 20, 100),("first aid", 15, 70)) 

# Run
python3 knapsack.py


# Video checking it works
https://youtu.be/otP8puv9fNE

# 5 Steps of Dynamic Programming applied to Knapsack Problem

### 1 Identify the subproblems 
If we have bags with capacities in range of 0 to n what would be the
maximum capacity that each bag can hold with and without the current
item.

### 2 Guess the first choice 
Add a random item into the knapsack

### 3 Recursively define the value of an optimal solution
Check the max when the item is in the bag and when the item is out

###  4 Compute the value of an optimal solution (recurse and memoize)
The recursion part is all the possible combination that can be added 
to the knapsack. 

### 5 Solve original problem by reconstructing the sub-problems 
When the weight is maxed out the value for possible options are calculated.
 

