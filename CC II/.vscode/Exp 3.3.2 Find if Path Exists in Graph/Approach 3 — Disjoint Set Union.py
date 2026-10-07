# ============================================================
#              FIND IF PATH EXISTS IN GRAPH
#                 DISJOINT SET UNION
#                    UNION-FIND
# ============================================================


class DisjointSet:

    def __init__(self, n):

        # Initially every node is its own parent
        self.parent = list(range(n))

        # Rank used to keep tree small
        self.rank = [0] * n

    # --------------------------------------------------------
    # Find operation with path compression
    # --------------------------------------------------------

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # --------------------------------------------------------
    # Union operation
    # --------------------------------------------------------

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        # Already in same component
        if root_x == root_y:
            return

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:

            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:

            self.parent[root_y] = root_x

        else:

            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def valid_path(n, edges, source, destination):

    # Create Disjoint Set
    ds = DisjointSet(n)

    # Connect all edges
    for u, v in edges:
        ds.union(u, v)

    # Check whether both belong
    # to the same connected component
    return ds.find(source) == ds.find(destination)


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
print("                  DISJOINT SET UNION")
print("                     UNION-FIND")
print("=" * 60)

print("\nNumber of Nodes :", n)
print("Edges           :", edges)
print("Source          :", source)
print("Destination     :", destination)

print("\n" + "-" * 60)
print("                    UNION OPERATIONS")
print("-" * 60)

ds = DisjointSet(n)

for u, v in edges:

    ds.union(u, v)

    print(f"union({u}, {v})")

print("\n" + "-" * 60)
print("                    FIND OPERATION")
print("-" * 60)

source_root = ds.find(source)
destination_root = ds.find(destination)

print(f"find({source})      = {source_root}")
print(f"find({destination}) = {destination_root}")

print("\n" + "-" * 60)
print("                         RESULT")
print("-" * 60)

result = source_root == destination_root

print("Path Exists :", result)

if result:
    print("Status      : Both nodes belong to the same component")
else:
    print("Status      : Nodes belong to different components")

print("\n" + "=" * 60)
print("                UNION-FIND COMPLETED")
print("=" * 60)