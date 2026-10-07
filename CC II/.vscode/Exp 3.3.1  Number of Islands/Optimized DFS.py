# ============================================================
#                  NUMBER OF ISLANDS
#                 OPTIMIZED DFS
# ============================================================

def num_islands(grid):

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):

        # Boundary and water check
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if grid[r][c] != '1':
            return

        # Mark land as visited
        grid[r][c] = '0'

        # Four directions
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right

    count = 0

    # Scan every cell
    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == '1':

                # New island found
                count += 1

                # Visit entire island
                dfs(r, c)

    return count


# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]


# ------------------------------------------------------------
# DISPLAY INPUT
# ------------------------------------------------------------

print("=" * 60)
print("                  NUMBER OF ISLANDS")
print("                   OPTIMIZED DFS")
print("=" * 60)

print("\nOriginal Grid:")

for row in grid:
    print("  " + " ".join(row))


# ------------------------------------------------------------
# SOLVE
# ------------------------------------------------------------

answer = num_islands(grid)


# ------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------

print("\n" + "-" * 60)
print("                       RESULT")
print("-" * 60)

print("Number of Islands :", answer)

print("\n" + "-" * 60)
print("                  AFTER DFS SINKING")
print("-" * 60)

for row in grid:
    print("  " + " ".join(row))

print("\n" + "-" * 60)
print("                    COMPLEXITY")
print("-" * 60)

print("Time Complexity  : O(m × n)")
print("Space Complexity : O(m × n) recursion stack")

print("\n" + "=" * 60)
print("             OPTIMIZED DFS COMPLETED")
print("=" * 60)