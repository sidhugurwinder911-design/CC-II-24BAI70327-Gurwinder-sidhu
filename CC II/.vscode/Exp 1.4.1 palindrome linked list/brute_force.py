# Palindrome Linked List - Brute Force

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList():
    n = int(input("Enter number of nodes: "))

    head = None
    current = None

    for i in range(n):
        value = int(input(f"Enter value for node {i + 1}: "))

        newNode = ListNode(value)

        if head is None:
            head = newNode
            current = head
        else:
            current.next = newNode
            current = current.next

    return head


def isPalindrome(head):
    values = []

    current = head

    while current:
        values.append(current.val)
        current = current.next

    left = 0
    right = len(values) - 1

    while left < right:
        if values[left] != values[right]:
            return False

        left += 1
        right -= 1

    return True


# Create linked list
head = createLinkedList()

# Check palindrome
result = isPalindrome(head)

if result:
    print("Output: true")
    print("The linked list is a palindrome.")
else:
    print("Output: false")
    print("The linked list is not a palindrome.")