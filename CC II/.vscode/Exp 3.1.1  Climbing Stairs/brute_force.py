# ============================================================
#              CLIMBING STAIRS - BRUTE FORCE
# ============================================================

import time


def climb_brute_force(n):
    if n <= 2:
        return n

    return climb_brute_force(n - 1) + climb_brute_force(n - 2)


print("=" * 60)
print("              CLIMBING STAIRS")
print("                 BRUTE FORCE")
print("=" * 60)

n = int(input("Enter number of stairs (1-45): "))

if n < 1 or n > 45:
    print("Invalid input! Enter a number between 1 and 45.")
else:

    start = time.perf_counter()

    answer = climb_brute_force(n)

    end = time.perf_counter()

    print("\n" + "-" * 60)
    print("                 RESULT")
    print("-" * 60)

    print(f"Number of stairs   : {n}")
    print(f"Number of ways     : {answer}")
    print(f"Execution time     : {end - start:.8f} seconds")

    print("\nComplexity:")
    print("Time Complexity    : O(2^n)")
    print("Space Complexity   : O(n)")

    print("-" * 60)
    print("Brute Force completed successfully!")
    print("=" * 60)