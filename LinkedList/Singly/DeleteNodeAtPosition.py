def deleteNode(llist, position):
    if position == 0:
        return llist.next

    current = llist
    index = 0

    while index != position - 1:
        current = current.next
        index += 1

    current.next = current.next.next

    return llist
