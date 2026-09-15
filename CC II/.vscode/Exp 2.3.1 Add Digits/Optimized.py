# ============================================================
# CC-II (24CSP-339)
# Experiment 2.3 - Add Digits
# Optimized Approach using Digital Root
# ============================================================

def add_digits_optimized(num):

    print("\n" + "=" * 60)
    print("           OPTIMIZED ADD DIGITS")
    print("              DIGITAL ROOT")
    print("=" * 60)

    print(f"Input Number : {num}")
    print("-" * 60)

    # Special case for 0
    if num == 0:
        print("Step 1 : Number is 0")
        print("Step 2 : Digital Root = 0")
        print("-" * 60)
        print("Final Answer : 0")
        print("=" * 60)
        return 0

    # Step 1
    print("Step 1 : Apply Digital Root Formula")
    print("         Answer = 1 + (num - 1) % 9")

    # Step 2
    num_minus_one = num - 1
    print(f"\nStep 2 : num - 1")
    print(f"         {num} - 1 = {num_minus_one}")

    # Step 3
    remainder = num_minus_one % 9
    print(f"\nStep 3 : Calculate {num_minus_one} % 9")
    print(f"         Remainder = {remainder}")

    # Step 4
    result = 1 + remainder
    print("\nStep 4 : Add 1")
    print(f"         1 + {remainder} = {result}")

    # Final answer
    print("\n" + "-" * 60)
    print(f"Final Answer : {result}")
    print("Time Complexity : O(1)")
    print("Space Complexity: O(1)")
    print("=" * 60)

    return result


# ============================================================
# Main Program
# ============================================================

print("\n" + "*" * 60)
print("       CC-II (24CSP-339) - EXPERIMENT 2.3")
print("                    ADD DIGITS")
print("*" * 60)

num = int(input("\nEnter a non-negative integer: "))

if num < 0:
    print("\nError: Please enter a non-negative integer.")
else:
    add_digits_optimized(num)