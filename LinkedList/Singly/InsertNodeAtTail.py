from LinkedList import SinglyLinkedListNode


def insertNodeAtTail(head, data):
    if head:
        current = head
        while current.next:
            current = current.next

        current.next = SinglyLinkedListNode(data)

        return head

    else:
        return SinglyLinkedListNode(data)
