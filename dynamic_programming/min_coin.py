coins = [1, 2, 5]
amount = 11

dp = [float('inf')] * (amount+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, amount+1):
        dp[i] = min(dp[i], 1 + dp[i-coin])

if dp[amount] == float('inf'):
    print("Not possible")
else:
    print("Minimum coins:", dp[amount])
    