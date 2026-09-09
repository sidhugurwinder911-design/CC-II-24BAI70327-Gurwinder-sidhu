class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Optimized DFS approach
def find_lca(root, p, q):
    if root is None:
        return None

    if root.value == p or root.value == q:
        return root

    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)

    if left and right:
        return root

    return left if left else right


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

lca = find_lca(root, p, q)

print("=" * 45)
print("       LOWEST COMMON ANCESTOR")
print("           OPTIMIZED APPROACH")
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

print("Lowest Common Ancestor =", lca.value)

print("-" * 45)
print(f"Result: LCA of {p} and {q} is {lca.value}.")
print("Time Complexity  : O(n)")
print("Space Complexity : O(h)")
print("-" * 45)

print("          EXPERIMENT COMPLETED")
print("=" * 45)