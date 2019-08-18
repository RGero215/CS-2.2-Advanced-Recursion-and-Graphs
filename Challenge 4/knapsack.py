def knapsack(items, capacity):
    ''' 
    A  method to determine the maximum value of the items included in the knapsack 
    without exceeding the capacity  C
    Run O(nc) time | O(nc) space where n is the number of items
    c is the capacity of the bag
    '''
    result = []
    knapsack_values = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        current_weight = items[i - 1][1]
        current_value = items[i - 1][2]
        for c in range(0, capacity + 1):
            if current_weight > c:
                knapsack_values[i][c] = knapsack_values[i - 1][c]
            else:
                knapsack_values[i][c] = max(knapsack_values[i - 1][c], knapsack_values[i - 1][c - current_weight] + current_value)
    
    for item in get_knapsack_items(items, knapsack_values):
        result.append(items[item])
    
    return [f'total value: {knapsack_values[-1][-1]}',result]

def get_knapsack_items(items, knapsack_values):
    '''
    Helper function to get the items and the values.
    '''
    sequence = []
    i = len(knapsack_values) - 1
    c = len(knapsack_values[0]) - 1

    while i > 0:
        if knapsack_values[i][c] == knapsack_values[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))


items = [["boot", 10, 60], ["tent", 20, 100],["water", 30, 120] ,["first aid", 15, 70]]
print('The items included in the knapsack for this optimal solution are')
print(knapsack(items, 50))