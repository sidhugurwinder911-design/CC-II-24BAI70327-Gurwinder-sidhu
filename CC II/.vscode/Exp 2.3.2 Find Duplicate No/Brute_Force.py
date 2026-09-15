# ============================================================
# CC-II (24CSP-339)
# Find the Duplicate Number
# Brute Force Approach - Using Hash Set
# ============================================================

def find_duplicate_brute_force(nums):

    seen = set()

    print("\n" + "=" * 60)
    print("       FIND DUPLICATE NUMBER - BRUTE FORCE")
    print("=" * 60)

    print(f"Input Array : {nums}")
    print("-" * 60)

    for i, num in enumerate(nums):

        print(f"Step {i + 1}: Checking {num}")

        if num in seen:
            print(f"         {num} is already present in {seen}")
            print(f"         Duplicate Found = {num}")
            print("-" * 60)
            return num

        seen.add(num)
        print(f"         Added {num} to seen set → {seen}")

    return -1


# ================= MAIN PROGRAM =================

print("\n" + "*" * 60)
print("       CC-II (24CSP-339) - FIND DUPLICATE NUMBER")
print("              BRUTE FORCE APPROACH")
print("*" * 60)

nums = [1, 3, 4, 2, 2]

result = find_duplicate_brute_force(nums)

print("\n" + "=" * 60)
print(f"Final Duplicate Number : {result}")
print("Time Complexity        : O(n)")
print("Space Complexity       : O(n)")
print("=" * 60)