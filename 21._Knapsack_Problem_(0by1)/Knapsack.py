def knapsack(values, weights, capacity):
    n = len(values)
    # Create a 2D array to store the maximum value that can be obtained
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Get the number of items from the user
num_items = int(input("Enter the number of items: "))

# Get the values of the items from the user
values = list(map(int, input("Enter the values of the items separated by space: ").split()))

# Get the weights of the items from the user
weights = list(map(int, input("Enter the weights of the items separated by space: ").split()))

# Get the maximum capacity of the knapsack from the user
capacity = int(input("Enter the maximum capacity of the knapsack: "))

# Perform the knapsack algorithm
max_value = knapsack(values, weights, capacity)

# Print the maximum value that can be obtained
print("The maximum value that can be obtained is:", max_value)
