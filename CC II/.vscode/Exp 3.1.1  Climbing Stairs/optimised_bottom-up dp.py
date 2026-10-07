# ============================================================
#          CLIMBING STAIRS - OPTIMIZED DYNAMIC PROGRAMMING
# ============================================================

import time


def climb_optimized(n):
    if n <= 2:
        return n

    prev1 = 1
    prev2 = 2

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current

    return prev2


print("=" * 60)
print("              CLIMBING STAIRS")
print("           OPTIMIZED DYNAMIC PROGRAMMING")
print("=" * 60)

n = int(input("Enter number of stairs (1-45): "))

if n < 1 or n > 45:
    print("Invalid input! Enter a number between 1 and 45.")
else:

    start = time.perf_counter()

    answer = climb_optimized(n)

    end = time.perf_counter()

    print("\n" + "-" * 60)
    print("                 RESULT")
    print("-" * 60)

    print(f"Number of stairs   : {n}")
    print(f"Number of ways     : {answer}")
    print(f"Execution time     : {end - start:.8f} seconds")

    print("\nDP Progression:")

    if n >= 1:
        print("ways(1) = 1")

    if n >= 2:
        print("ways(2) = 2")

    prev1 = 1
    prev2 = 2

    for i in range(3, n + 1):
        current = prev1 + prev2
        print(f"ways({i}) = {prev1} + {prev2} = {current}")
        prev1 = prev2
        prev2 = current

    print("\nComplexity:")
    print("Time Complexity    : O(n)")
    print("Space Complexity   : O(1)")

    print("-" * 60)
    print("Optimized DP completed successfully!")
    print("=" * 60)