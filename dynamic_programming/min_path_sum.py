grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

rows = len(grid)
cols = len(grid[0])

dp = [[0] * cols for _ in range(rows)]

dp[0][0] = grid[0][0]

for i in range(1, rows):
    dp[i][0] = dp[i-1][0] + grid[i][0]

for j in range(1, cols):
    dp[0][j] = dp[0][j-1] + grid[0][j]

for i in range(1, rows):
    for j in range(1, cols):
        dp[i][j] = grid[i][j] + min(
            dp[i-1][j],
            dp[i][j-1]
        )

print("Minimum Path Sum:", dp[-1][-1])