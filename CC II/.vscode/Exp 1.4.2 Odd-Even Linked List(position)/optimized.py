# Odd-Even Linked List - Optimized Approach

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def oddEvenList(head):
    if head is None or head.next is None:
        return head

    # Odd pointer starts at first node
    odd = head

    # Even pointer starts at second node
    even = head.next

    # Save the first even node
    evenHead = even

    # Rearrange the links
    while even is not None and even.next is not None:

        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    # Connect odd list with even list
    odd.next = evenHead

    return head


# Taking input from user
values = list(map(int, input("Enter linked list elements: ").split()))


# Creating the linked list
head = None
tail = None

for value in values:
    newNode = ListNode(value)

    if head is None:
        head = newNode
        tail = newNode
    else:
        tail.next = newNode
        tail = newNode


# Display original linked list
print("Original Linked List:", end=" ")

current = head

while current is not None:
    print(current.val, end=" ")
    current = current.next


# Apply Odd-Even Linked List
res = oddEvenList(head)


# Display the result
print("\nOdd-Even Linked List:", end=" ")

while res is not None:
    print(res.val, end=" ")
    res = res.next

print()