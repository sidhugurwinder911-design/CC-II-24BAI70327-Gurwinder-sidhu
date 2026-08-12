# Odd-Even Linked List - Brute Force

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list_brute(head):
    if not head:
        return None

    odd = []
    even = []

    position = 1
    current = head

    # Separate nodes based on their positions
    while current:
        if position % 2 == 1:
            odd.append(current.val)
        else:
            even.append(current.val)

        current = current.next
        position += 1

    # Combine odd-position and even-position values
    result = odd + even

    # Create a new linked list
    new_head = None
    tail = None

    for value in result:
        new_node = ListNode(value)

        if new_head is None:
            new_head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return new_head


# Taking input from user
values = list(map(int, input("Enter linked list elements: ").split()))

# Creating linked list
head = None
tail = None

for value in values:
    new_node = ListNode(value)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node


# Display original linked list
print("Original Linked List:", end=" ")

current = head
while current:
    print(current.val, end=" ")
    current = current.next


# Apply brute force method
result = odd_even_list_brute(head)

# Display result
print("\nOdd-Even Linked List:", end=" ")

while result:
    print(result.val, end=" ")
    result = result.next

print()