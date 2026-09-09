class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_successor(root, p):
    successor = None
    current = root

    while current is not None:
        if p.value >= current.value:
            current = current.right
        else:
            successor = current
            current = current.left

    return successor


# Create BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

# Node p
p = root.left

successor = inorder_successor(root, p)

print("=" * 45)
print("       IN-ORDER SUCCESSOR")
print("          OPTIMIZED")
print("=" * 45)

print("\nBST:")
print("""
              5
            /   \\
           3     6
          / \\
         2   4
        /
       1
""")

print("-" * 45)
print("Node p :", p.value)

if successor:
    print("In-order Successor :", successor.value)
else:
    print("In-order Successor : None")

print("-" * 45)
print("Time Complexity  : O(h)")
print("Space Complexity : O(1)")
print("=" * 45)