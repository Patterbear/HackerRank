def removeDuplicates(llist):
    current = llist

    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return llist
