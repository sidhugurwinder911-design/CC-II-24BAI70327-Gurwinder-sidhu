# ============================================================
#              FIND IF PATH EXISTS IN GRAPH
#                         BFS
# ============================================================

from collections import deque


def valid_path(n, edges, source, destination):

    # --------------------------------------------------------
    # Step 1: Build adjacency list
    # --------------------------------------------------------

    adj = [[] for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # --------------------------------------------------------
    # Step 2: Source and destination are same
    # --------------------------------------------------------

    if source == destination:
        return True

    # --------------------------------------------------------
    # Step 3: Create visited array and queue
    # --------------------------------------------------------

    visited = [False] * n

    queue = deque([source])
    visited[source] = True

    # --------------------------------------------------------
    # Step 4: BFS traversal
    # --------------------------------------------------------

    while queue:

        node = queue.popleft()

        for neighbour in adj[node]:

            # Destination reached
            if neighbour == destination:
                return True

            # Visit unvisited neighbour
            if not visited[neighbour]:

                visited[neighbour] = True
                queue.append(neighbour)

    # Destination not reachable
    return False


# ============================================================
#                       TEST CASE
# ============================================================

n = 3

edges = [
    [0, 1],
    [1, 2],
    [2, 0]
]

source = 0
destination = 2


# ============================================================
#                       OUTPUT
# ============================================================

print("=" * 60)
print("              FIND IF PATH EXISTS IN GRAPH")
print("                         BFS")
print("=" * 60)

print("\nNumber of Nodes :", n)
print("Edges           :", edges)
print("Source          :", source)
print("Destination     :", destination)

print("\n" + "-" * 60)
print("                       BFS TRAVERSAL")
print("-" * 60)

print("Starting from source node:", source)
print("Exploring graph level by level...")

result = valid_path(n, edges, source, destination)

print("\n" + "-" * 60)
print("                         RESULT")
print("-" * 60)

print("Path Exists :", result)

if result:
    print("Status      : Destination is reachable")
else:
    print("Status      : No path exists")

print("\n" + "=" * 60)
print("                    BFS COMPLETED")
print("=" * 60)