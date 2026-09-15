# ============================================================
# CC-II (24CSP-339)
# Experiment 2.3 - Add Digits
# Brute Force / Simulation Approach
# ============================================================

def add_digits_brute_force(num):
    print("\n" + "=" * 55)
    print("          ADD DIGITS - BRUTE FORCE")
    print("=" * 55)
    print(f"Input Number : {num}")
    print("-" * 55)

    step = 1

    while num >= 10:
        original = num
        total = 0
        digits = []

        # Extract and add digits
        temp = num

        while temp > 0:
            digit = temp % 10
            digits.append(digit)
            total += digit
            temp //= 10

        digits.reverse()

        print(f"Step {step}: {original} → {' + '.join(map(str, digits))} = {total}")

        num = total
        step += 1

    print("-" * 55)
    print(f"Digital Root : {num}")
    print("=" * 55)

    return num


# ---------------- Main Program ----------------

print("\n" + "*" * 55)
print("       CC-II (24CSP-339) - EXPERIMENT 2.3")
print("                 ADD DIGITS")
print("*" * 55)

num = int(input("\nEnter a non-negative integer: "))

if num < 0:
    print("\nError: Please enter a non-negative integer.")
else:
    result = add_digits_brute_force(num)
    print(f"\nFinal Answer = {result}")