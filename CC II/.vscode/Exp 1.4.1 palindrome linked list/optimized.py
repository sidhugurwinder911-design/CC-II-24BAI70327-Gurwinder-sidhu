# Palindrome Linked List
# Optimized Approach: Reverse Second Half

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):

        # Find the middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev, curr = None, slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second_head = prev

        # Compare first half and reversed second half
        p1, p2 = head, second_head

        while p2:
            if p1.val != p2.val:
                return False, second_head

            p1 = p1.next
            p2 = p2.next

        return True, second_head


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


def printLinkedList(head):
    values = []
    current = head

    while current:
        values.append(str(current.val))
        current = current.next

    print(" → ".join(values))


# Create linked list
head = createLinkedList()

print("\nOriginal Linked List:")
printLinkedList(head)

# Check palindrome
solution = Solution()
result, reversed_head = solution.isPalindrome(head)

print("\nReversed Second Half:")
printLinkedList(reversed_head)

if result:
    print("\nOutput: true")
    print("The linked list is a palindrome.")
else:
    print("\nOutput: false")
    print("The linked list is not a palindrome.")