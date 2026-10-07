# ============================================================
#              FROG JUMP WITH K DISTANCE
#              OPTIMIZED DYNAMIC PROGRAMMING
# ============================================================

def frog_jump(height, k):
    n = len(height)

    dp = [0] * n

    for i in range(1, n):
        minimum_cost = float('inf')

        for j in range(max(0, i - k), i):
            cost = dp[j] + abs(height[i] - height[j])
            minimum_cost = min(minimum_cost, cost)

        dp[i] = minimum_cost

    return dp


# Input
height = [10, 30, 40, 50, 20]
k = 3

# Calculate DP table
dp = frog_jump(height, k)

answer = dp[-1]


# Output
print("=" * 60)
print("                FROG JUMP")
print("             OPTIMIZED DP")
print("=" * 60)

print("\nHeights :", height)
print("Maximum Jump Distance (k) :", k)

print("\n" + "-" * 60)
print("                    DP TABLE")
print("-" * 60)

print(f"{'Stone':<10}{'Height':<12}{'Minimum Cost':<15}")
print("-" * 60)

for i in range(len(height)):
    print(f"{i:<10}{height[i]:<12}{dp[i]:<15}")

print("-" * 60)

print("\nFinal Result:")
print("Minimum Cost :", answer)

print("\nThe frog reaches the last stone")
print("with the minimum possible cost of", answer)

print("\nComplexity:")
print("Time Complexity  : O(n × k)")
print("Space Complexity : O(n)")

print("\n" + "=" * 60)
print("             OPTIMIZED DP COMPLETED")
print("=" * 60)