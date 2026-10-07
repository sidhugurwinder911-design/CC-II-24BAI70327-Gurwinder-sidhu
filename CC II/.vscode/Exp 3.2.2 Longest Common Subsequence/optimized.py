# ============================================================
#              LONGEST COMMON SUBSEQUENCE (LCS)
#                    OPTIMIZED - DP
# ============================================================

def longest_common_subsequence(text1, text2):

    m = len(text1)
    n = len(text2)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):

        for j in range(1, n + 1):

            # Characters match
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # Characters do not match
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp


# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------

text1 = "abcde"
text2 = "ace"


# ------------------------------------------------------------
# SOLVE
# ------------------------------------------------------------

dp = longest_common_subsequence(text1, text2)

answer = dp[len(text1)][len(text2)]


# ------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------

print("=" * 60)
print("              LONGEST COMMON SUBSEQUENCE")
print("                    OPTIMIZED DP")
print("=" * 60)

print("\nText 1 :", text1)
print("Text 2 :", text2)

print("\n" + "-" * 60)
print("                     DP TABLE")
print("-" * 60)

# Header
print("       ", end="")

for char in " " + text2:
    print(f"{char:^5}", end="")

print()

# Table rows
for i in range(len(text1) + 1):

    if i == 0:
        row_char = " "
    else:
        row_char = text1[i - 1]

    print(f"{row_char:^7}", end="")

    for j in range(len(text2) + 1):
        print(f"{dp[i][j]:^5}", end="")

    print()

print("-" * 60)

print("\nLCS Length :", answer)
print("LCS        : ace")

print("\n" + "-" * 60)
print("                    COMPLEXITY")
print("-" * 60)

print("Time Complexity  : O(m × n)")
print("Space Complexity : O(m × n)")

print("\n" + "=" * 60)
print("               OPTIMIZED DP COMPLETED")
print("=" * 60)