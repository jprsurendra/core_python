class Node:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data  # Data to store in the node
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node


class DoublyLinkedList:
    """A doubly linked list."""
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
        new_node.prev = current

    def prepend(self, data):
        """Add a new node to the beginning of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        """Delete the first node with the given data."""
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            if current.next:
                current.next.prev = None
            self.head = current.next
            current = None
            return

        # Find the node to be deleted
        while current and current.data != key:
            current = current.next

        # If the key was not found
        if not current:
            print("Key not found!")
            return

        # Remove the node
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        current = None

    def display(self):
        """Display all the nodes in the list from head to tail."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_reverse(self):
        """Display all the nodes in the list from tail to head."""
        current = self.head
        if not current:
            print("None")
            return
        # Move to the tail
        while current.next:
            current = current.next
        # Traverse backward
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("Doubly Linked List:")
dll.display()

print("\nAdding 5 to the beginning:")
dll.prepend(5)
dll.display()

print("\nDeleting 20:")
dll.delete(20)
dll.display()

print("\nDisplaying in reverse:")
dll.display_reverse()
