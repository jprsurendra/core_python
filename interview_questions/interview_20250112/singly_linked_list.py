class Node:
    """A node in a linked list."""
    def __init__(self, data):
        self.data = data  # Data to store in the node
        self.next = None  # Pointer to the next node


class LinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None  # The first node of the linked list

    def append(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    def display(self):
        """Display all the nodes in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, key):
        """Delete the first node with the given data."""
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Find the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print("Key not found!")
            return

        # Remove the node
        prev.next = current.next
        current = None


# Example usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("Linked List:")
linked_list.display()

print("\nDeleting 20:")
linked_list.delete(20)
linked_list.display()

print("\nDeleting 40 (not in list):")
linked_list.delete(40)
linked_list.display()
