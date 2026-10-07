# ============================================================
#                    COIN CHANGE
#                     BRUTE FORCE
# ============================================================

def coin_change(coins, amount):

    # Base Case
    if amount == 0:
        return 0

    minimum = float('inf')

    # Try every possible coin
    for coin in coins:

        if coin <= amount:

            result = coin_change(coins, amount - coin)

            if result != float('inf'):
                minimum = min(minimum, result + 1)

    return minimum


# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------

coins = [1, 2, 5]
amount = 11


# ------------------------------------------------------------
# SOLVE
# ------------------------------------------------------------

answer = coin_change(coins, amount)


# ------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------

print("=" * 60)
print("                    COIN CHANGE")
print("                     BRUTE FORCE")
print("=" * 60)

print("\nCoins  :", coins)
print("Amount :", amount)

print("\n" + "-" * 60)
print("                       RESULT")
print("-" * 60)

if answer == float('inf'):
    print("Minimum Coins : -1")
    print("Status        : Amount cannot be formed")
else:
    print("Minimum Coins :", answer)
    print("Status        : Amount can be formed")

print("\n" + "-" * 60)
print("                    COMPLEXITY")
print("-" * 60)

print("Time Complexity  : O(c^amount)")
print("Space Complexity : O(amount)")

print("\n" + "=" * 60)
print("              BRUTE FORCE COMPLETED")
print("=" * 60)