def getNode(llist, positionFromTail):
    current = llist
    length = 0

    while current:
        current = current.next
        length += 1

    target_index = length - 1 - positionFromTail
    index = 0

    current = llist

    while index != target_index:
        current = current.next
        index += 1

    return current.data
