# ============================================================
# CC-II (24CSP-339)
# Find the Duplicate Number
# Optimized Approach - Floyd's Tortoise and Hare Algorithm
# ============================================================

def find_duplicate_optimized(nums):

    print("\n" + "=" * 65)
    print("    FIND DUPLICATE NUMBER - FLOYD'S CYCLE DETECTION")
    print("=" * 65)

    print(f"Input Array : {nums}")

    # --------------------------------------------------------
    # PHASE 1: Find meeting point
    # --------------------------------------------------------

    print("\nPHASE 1: FIND THE MEETING POINT")
    print("-" * 65)

    slow = nums[0]
    fast = nums[0]

    print(f"Initial Slow = nums[0] = {slow}")
    print(f"Initial Fast = nums[0] = {fast}")

    step = 1

    while True:

        # Slow moves one step
        slow = nums[slow]

        # Fast moves two steps
        fast = nums[nums[fast]]

        print(f"\nStep {step}:")
        print(f"Slow moves 1 step → {slow}")
        print(f"Fast moves 2 steps → {fast}")

        if slow == fast:
            print(f"\n✓ Slow and Fast meet at {slow}")
            break

        step += 1

    # --------------------------------------------------------
    # PHASE 2: Find cycle entrance
    # --------------------------------------------------------

    print("\n" + "=" * 65)
    print("PHASE 2: FIND THE DUPLICATE NUMBER")
    print("-" * 65)

    slow = nums[0]

    print(f"Reset Slow = nums[0] = {slow}")
    print(f"Fast remains at = {fast}")

    step = 1

    while slow != fast:

        slow = nums[slow]
        fast = nums[fast]

        print(f"\nStep {step}:")
        print(f"Slow moves → {slow}")
        print(f"Fast moves → {fast}")

        step += 1

    print("\n" + "-" * 65)
    print(f"✓ Slow and Fast meet at {slow}")
    print(f"✓ Duplicate Number = {slow}")
    print("=" * 65)

    return slow


# ================= MAIN PROGRAM =================

print("\n" + "*" * 65)
print("       CC-II (24CSP-339) - FIND DUPLICATE NUMBER")
print("              OPTIMIZED APPROACH")
print("*" * 65)

nums = [1, 3, 4, 2, 2]

result = find_duplicate_optimized(nums)

print("\n" + "=" * 65)
print(f"FINAL ANSWER : {result}")
print("Algorithm    : Floyd's Tortoise and Hare")
print("Time         : O(n)")
print("Extra Space  : O(1)")
print("=" * 65)