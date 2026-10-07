# ============================================================
#              FROG JUMP WITH K DISTANCE
#                   BRUTE FORCE
# ============================================================

def frog_jump(height, k, i):
    if i == 0:
        return 0

    minimum_cost = float('inf')

    for j in range(max(0, i - k), i):
        cost = frog_jump(height, k, j) + abs(height[i] - height[j])
        minimum_cost = min(minimum_cost, cost)

    return minimum_cost


# Input
height = [10, 30, 40, 50, 20]
k = 3

# Calculate minimum cost
answer = frog_jump(height, k, len(height) - 1)


# Output
print("=" * 55)
print("              FROG JUMP")
print("               BRUTE FORCE")
print("=" * 55)

print("\nHeights :", height)
print("Maximum Jump Distance (k) :", k)

print("\n" + "-" * 55)
print("                    RESULT")
print("-" * 55)

print("Minimum Cost :", answer)

print("\nThe frog reaches the last stone")
print("with the minimum possible cost of", answer)

print("\nComplexity:")
print("Time Complexity  : O(k^n)")
print("Space Complexity : O(n)")

print("\n" + "=" * 55)
print("              BRUTE FORCE COMPLETED")
print("=" * 55)