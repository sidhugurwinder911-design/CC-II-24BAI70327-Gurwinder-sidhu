# ============================================================
#              FIND IF PATH EXISTS IN GRAPH
#                         DFS
# ============================================================


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
    # Step 3: Visited array
    # --------------------------------------------------------

    visited = [False] * n

    # --------------------------------------------------------
    # Step 4: DFS function
    # --------------------------------------------------------

    def dfs(node):

        # Destination reached
        if node == destination:
            return True

        visited[node] = True

        # Explore neighbours
        for neighbour in adj[node]:

            if not visited[neighbour]:

                if dfs(neighbour):
                    return True

        return False

    # Start DFS
    return dfs(source)


# ============================================================
#                       TEST CASE
# ============================================================

n = 6

edges = [
    [0, 1],
    [0, 2],
    [3, 5],
    [5, 4],
    [4, 3]
]

source = 0
destination = 5


# ============================================================
#                       OUTPUT
# ============================================================

print("=" * 60)
print("              FIND IF PATH EXISTS IN GRAPH")
print("                         DFS")
print("=" * 60)

print("\nNumber of Nodes :", n)
print("Edges           :", edges)
print("Source          :", source)
print("Destination     :", destination)

print("\n" + "-" * 60)
print("                       DFS TRAVERSAL")
print("-" * 60)

print("Starting DFS from node:", source)
print("Exploring graph depth-first...")

result = valid_path(n, edges, source, destination)

print("\n" + "-" * 60)
print("                         RESULT")
print("-" * 60)

print("Path Exists :", result)

if result:
    print("Status      : Destination is reachable")
else:
    print("Status      : Destination cannot be reached")

print("\n" + "=" * 60)
print("                    DFS COMPLETED")
print("=" * 60)