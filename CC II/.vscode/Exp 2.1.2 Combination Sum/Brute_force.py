class Solution:
    def combinationSum(self, candidates, target):
        result = set()

        def brute_force(remaining, current):
            # Target reached
            if remaining == 0:
                result.add(tuple(sorted(current)))
                return

            # Target exceeded
            if remaining < 0:
                return

            # Try every candidate
            for num in candidates:
                current.append(num)
                brute_force(remaining - num, current)
                current.pop()

        brute_force(target, [])

        return [list(x) for x in sorted(result)]


# Main Program
candidates = [2, 3, 5]
target = 8

solution = Solution()
result = solution.combinationSum(candidates, target)

print("=" * 50)
print("       COMBINATION SUM - BRUTE FORCE")
print("=" * 50)

print("Candidates :", candidates)
print("Target     :", target)

print("\nValid Combinations:")
print("-" * 50)

if result:
    for i, combination in enumerate(result, 1):
        print(f"{i}. {combination}  -> Sum = {sum(combination)}")
else:
    print("No valid combinations found.")

print("-" * 50)
print("Total Combinations:", len(result))
print("=" * 50)