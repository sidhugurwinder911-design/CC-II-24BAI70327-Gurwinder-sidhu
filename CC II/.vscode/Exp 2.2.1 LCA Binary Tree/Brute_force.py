class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_path(root, target, path):
    if root is None:
        return False

    path.append(root)

    if root.value == target:
        return True

    if find_path(root.left, target, path) or find_path(root.right, target, path):
        return True

    path.pop()
    return False


def find_lca(root, p, q):
    path_p = []
    path_q = []

    find_path(root, p, path_p)
    find_path(root, q, path_q)

    i = 0
    while i < len(path_p) and i < len(path_q):
        if path_p[i].value != path_q[i].value:
            break
        i += 1

    return path_p[i - 1], path_p, path_q


# Create Binary Tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = 7
q = 4

lca, path_p, path_q = find_lca(root, p, q)

print("=" * 45)
print("       LOWEST COMMON ANCESTOR")
print("          BRUTE FORCE APPROACH")
print("=" * 45)

print("""
Binary Tree:

              3
            /   \\
           5     1
          / \\   / \\
         6   2 0   8
            / \\
           7   4
""")

print("-" * 45)
print("Target Node P :", p)
print("Target Node Q :", q)
print("-" * 45)

print("Path from Root to P :", " -> ".join(str(x.value) for x in path_p))
print("Path from Root to Q :", " -> ".join(str(x.value) for x in path_q))

print("-" * 45)
print("Lowest Common Ancestor =", lca.value)
print("-" * 45)

print(f"Result: LCA of {p} and {q} is {lca.value}.")

print("=" * 45)
print("          EXPERIMENT COMPLETED")
print("=" * 45)