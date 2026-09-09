class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root, order):
    if root is None:
        return

    inorder(root.left, order)
    order.append(root)
    inorder(root.right, order)


def inorder_successor(root, p):
    order = []
    inorder(root, order)

    for i in range(len(order)):
        if order[i].value == p.value:
            if i + 1 < len(order):
                return order[i + 1]
            return None

    return None


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
print("          BRUTE FORCE")
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
print("Time Complexity  : O(n)")
print("Space Complexity : O(n)")
print("=" * 45)