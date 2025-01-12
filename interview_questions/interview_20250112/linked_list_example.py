from interview_questions.interview_20250112.singly_linked_list import LinkedList


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print("Linked List:")
    linked_list.display()

    reverse_linked_list(linked_list.head)

    print("Reverse Linked List:")
    linked_list.display()
