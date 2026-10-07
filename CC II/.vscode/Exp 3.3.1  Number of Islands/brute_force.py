# ============================================================
#                  NUMBER OF ISLANDS
#                    BRUTE FORCE
# ============================================================

def explore(grid, r, c, visited):
    rows = len(grid)
    cols = len(grid[0])

    # Boundary check
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return

    # Water or already visited
    if grid[r][c] == '0' or visited[r][c]:
        return

    visited[r][c] = True

    # Four directions
    explore(grid, r - 1, c, visited)  # Up
    explore(grid, r + 1, c, visited)  # Down
    explore(grid, r, c - 1, visited)  # Left
    explore(grid, r, c + 1, visited)  # Right


def find_component(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    explore(grid, r, c, visited)

    # Find the first/top-left cell of this island
    representative = None

    for i in range(rows):
        for j in range(cols):
            if visited[i][j]:
                if representative is None:
                    representative = (i, j)

    return representative


def count_islands(grid):

    rows = len(grid)
    cols = len(grid[0])

    count = 0

    # Every land cell starts a new traversal
    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == '1':

                representative = find_component(grid, r, c)

                # Count island only once
                if representative == (r, c):
                    count += 1

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
# SOLVE
# ------------------------------------------------------------

answer = count_islands(grid)


# ------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------

print("=" * 60)
print("                  NUMBER OF ISLANDS")
print("                     BRUTE FORCE")
print("=" * 60)

print("\nInput Grid:")

for row in grid:
    print("  " + " ".join(row))

print("\n" + "-" * 60)
print("                       RESULT")
print("-" * 60)

print("Number of Islands :", answer)

print("\n" + "-" * 60)
print("                    COMPLEXITY")
print("-" * 60)

print("Time Complexity  : O((m × n)^2)")
print("Space Complexity : O(m × n)")

print("\n" + "=" * 60)
print("              BRUTE FORCE COMPLETED")
print("=" * 60)