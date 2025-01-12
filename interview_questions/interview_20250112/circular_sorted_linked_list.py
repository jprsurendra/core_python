
'''
    Here’s an implementation of a circular sorted linked list in Python:

    Explanation:
        In a circular linked list, the last node points back to the head, forming a circle.
        In a sorted circular linked list, new nodes are inserted in a way that maintains the order of the list.

    Key Points:
        Circular Nature: The last node always points back to the head.
        Sorted Order: Elements are inserted in the correct order.
        Edge Cases: The implementation handles cases like inserting into an empty list, deleting the head, and deleting a non-existent element.
        Let me know if you need further customizations or explanations!

    Implementation:

'''
class Node:
    """A node in a circular linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSortedLinkedList:
    """A circular sorted linked list."""
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node while maintaining sorted order."""
        new_node = Node(data)

        # If the list is empty
        if not self.head:
            self.head = new_node
            new_node.next = new_node  # Point to itself
            return

        current = self.head

        # Case 1: Insert before the head (smallest element)
        if data < self.head.data:
            # Find the last node
            while current.next != self.head:
                current = current.next
            # Update the links
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

        # Case 2: Traverse the list to find the correct position
        while current.next != self.head and current.next.data < data:
            current = current.next

        # Insert the new node
        new_node.next = current.next
        current.next = new_node

    def display(self):
        """Display the circular linked list."""
        if not self.head:
            print("List is empty!")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

    def delete(self, key):
        """Delete the first node with the given data."""
        if not self.head:
            print("List is empty!")
            return

        current = self.head

        # Case 1: Deleting the head node
        if self.head.data == key:
            # Find the last node
            while current.next != self.head:
                current = current.next
            if self.head.next == self.head:  # Single node case
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return

        # Case 2: Deleting a non-head node
        prev = None
        while current.next != self.head and current.data != key:
            prev = current
            current = current.next

        if current.data == key:
            prev.next = current.next
        else:
            print("Key not found!")

# Example usage
circular_list = CircularSortedLinkedList()
circular_list.insert(30)
circular_list.insert(10)
circular_list.insert(20)
circular_list.insert(40)

print("Circular Sorted Linked List:")
circular_list.display()

print("\nDeleting 20:")
circular_list.delete(20)
circular_list.display()

print("\nDeleting 10 (head node):")
circular_list.delete(10)
circular_list.display()

print("\nDeleting 50 (not in list):")
circular_list.delete(50)
circular_list.display()
