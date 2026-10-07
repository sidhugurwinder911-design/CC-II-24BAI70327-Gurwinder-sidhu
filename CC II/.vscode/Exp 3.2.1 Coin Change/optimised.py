# ============================================================
#                    COIN CHANGE
#                    OPTIMIZED DP
# ============================================================

def coin_change(coins, amount):

    # DP array
    # dp[a] = minimum coins required to make amount 'a'
    dp = [amount + 1] * (amount + 1)

    # Base Case
    dp[0] = 0

    # Build DP table
    for a in range(1, amount + 1):

        for coin in coins:

            if coin <= a:
                dp[a] = min(
                    dp[a],
                    dp[a - coin] + 1
                )

    # Return result
    if dp[amount] <= amount:
        return dp, dp[amount]
    else:
        return dp, -1


# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------

coins = [1, 2, 5]
amount = 11


# ------------------------------------------------------------
# SOLVE
# ------------------------------------------------------------

dp, answer = coin_change(coins, amount)


# ------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------

print("=" * 60)
print("                    COIN CHANGE")
print("                    OPTIMIZED DP")
print("=" * 60)

print("\nCoins  :", coins)
print("Amount :", amount)

print("\n" + "-" * 60)
print("                       DP TABLE")
print("-" * 60)

print(f"{'Amount':<15}{'Minimum Coins':<20}")
print("-" * 60)

for i in range(amount + 1):

    if dp[i] > amount:
        value = "∞"
    else:
        value = dp[i]

    print(f"{i:<15}{value:<20}")

print("-" * 60)

print("\nMinimum Coins :", answer)

if answer == -1:
    print("Status        : Amount cannot be formed")
else:
    print("Status        : Amount can be formed")

print("\n" + "-" * 60)
print("                    COMPLEXITY")
print("-" * 60)

print("Time Complexity  : O(amount × c)")
print("Space Complexity : O(amount)")

print("\n" + "=" * 60)
print("              OPTIMIZED DP COMPLETED")
print("=" * 60)