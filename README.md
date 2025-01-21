# Day-21-Knapsack-Problem_-0-1-
Here's python program for Knapsack Problem. Day 21 of Day 365

 Problem Statement
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. Each item can be included or excluded (hence "0/1").

 Step-by-Step Explanation

1. Define the Inputs:
    - `N`: Number of items.
    - `W`: Maximum weight capacity of the knapsack.
    - `weight[]`: Array containing the weights of the items.
    - `value[]`: Array containing the values of the items.

2. Define the DP Array:
    - Create a 2D DP array, `dp[][]` where `dp[i][j]` represents the maximum value that can be obtained with the first `i` items and a maximum weight `j`.

3. Initialize the DP Array:
    - Set `dp[0][j] = 0` for all `j`, because with 0 items, the maximum value is 0.
    - Set `dp[i][0] = 0` for all `i`, because with 0 weight capacity, the maximum value is 0.

4. Fill the DP Array:
    - Iterate through all items and weights.
    - For each item `i` (from 1 to `N`) and each weight `w` (from 1 to `W`), determine if the item can be included or not.
    - If the weight of the current item `weight[i-1]` is less than or equal to the current weight `w`:
        - Include the item: `dp[i][w] = max(dp[i-1][w], value[i-1] + dp[i-1][w-weight[i-1]])`
        - Exclude the item: `dp[i][w] = dp[i-1][w]`
    - Otherwise, the item cannot be included, so just carry forward the value without the item: `dp[i][w] = dp[i-1][w]`

5. Result:
    - The value in `dp[N][W]` will be the maximum value that can be achieved with the given items and weight capacity.

 Example:

Let's say we have 3 items with the following weights and values:
- Item 1: weight = 1, value = 6
- Item 2: weight = 2, value = 10
- Item 3: weight = 3, value = 12

And the maximum weight capacity of the knapsack is 5.

Step-by-Step DP Table:

|     | w=0 | w=1 | w=2 | w=3 | w=4 | w=5 |
|-----|-----|-----|-----|-----|-----|-----|
| i=0 |  0  |  0  |  0  |  0  |  0  |  0  |
| i=1 |  0  |  6  |  6  |  6  |  6  |  6  |
| i=2 |  0  |  6  |  10 | 16  | 16  | 16  |
| i=3 |  0  |  6  |  10 | 16  | 18  | 22  |

- At `i=1` and `w=1`, we can include item 1, so `dp[1][1] = 6`.
- At `i=2` and `w=2`, we can include item 2, so `dp[2][2] = 10`.
- At `i=2` and `w=3`, we can include item 1 and item 2, so `dp[2][3] = 16`.
- At `i=3` and `w=4`, we can include item 1 and item 3, so `dp[3][4] = 18`.
- At `i=3` and `w=5`, we can include items 1, 2, and 3, so `dp[3][5] = 22`.

