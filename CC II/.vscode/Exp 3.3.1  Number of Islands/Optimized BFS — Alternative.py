# ============================================================
#                  NUMBER OF ISLANDS
#                 OPTIMIZED BFS
# ============================================================

from collections import deque


def num_islands(grid):

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    count = 0

    # Four directions
    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == '1':

                # New island
                count += 1

                # Queue for BFS
                queue = deque([(r, c)])

                # Mark starting cell visited
                grid[r][c] = '0'

                while queue:

                    current_r, current_c = queue.popleft()

                    # Explore four directions
                    for dr, dc in directions:

                        nr = current_r + dr
                        nc = current_c + dc

                        # Valid land cell
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == '1'
                        ):

                            # Mark visited
                            grid[nr][nc] = '0'

                            # Add to queue
                            queue.append((nr, nc))

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
print("                   OPTIMIZED BFS")
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
print("                    COMPLEXITY")
print("-" * 60)

print("Time Complexity  : O(m × n)")
print("Space Complexity : O(m × n)")

print("\n" + "=" * 60)
print("             OPTIMIZED BFS COMPLETED")
print("=" * 60)