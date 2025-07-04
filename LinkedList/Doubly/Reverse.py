def reverse(llist):
    current = llist

    while current:
        next = current.next
        current.next = current.prev
        current.prev = next

        new_head = current
        current = next

    return new_head
