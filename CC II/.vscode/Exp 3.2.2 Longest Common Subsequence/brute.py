# ============================================================
#              LONGEST COMMON SUBSEQUENCE (LCS)
#                       BRUTE FORCE
# ============================================================

def lcs_brute_force(text1, text2, i, j):

    # Base Case
    if i == len(text1) or j == len(text2):
        return 0

    # If characters match
    if text1[i] == text2[j]:
        return 1 + lcs_brute_force(text1, text2, i + 1, j + 1)

    # If characters do not match
    return max(
        lcs_brute_force(text1, text2, i + 1, j),
        lcs_brute_force(text1, text2, i, j + 1)
    )


# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------

text1 = "abcde"
text2 = "ace"


# ------------------------------------------------------------
# SOLVE
# ------------------------------------------------------------

answer = lcs_brute_force(text1, text2, 0, 0)


# ------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------

print("=" * 60)
print("              LONGEST COMMON SUBSEQUENCE")
print("                     BRUTE FORCE")
print("=" * 60)

print("\nText 1 :", text1)
print("Text 2 :", text2)

print("\n" + "-" * 60)
print("                       RESULT")
print("-" * 60)

print("LCS Length :", answer)

print("LCS        : ace")

print("\n" + "-" * 60)
print("                    COMPLEXITY")
print("-" * 60)

print("Time Complexity  : O(2^(m+n))")
print("Space Complexity : O(m+n)")

print("\n" + "=" * 60)
print("              BRUTE FORCE COMPLETED")
print("=" * 60)