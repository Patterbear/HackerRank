from LinkedList import DoublyLinkedListNode


def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)
    current = llist

    while current and current.data < data:
        current = current.next

    if current:
        new_node.next = current
        new_node.prev = current.prev
        if current.prev:
            current.prev.next = new_node
        else:
            llist = new_node
        current.prev = new_node
    else:
        tail = llist
        while tail.next:
            tail = tail.next
        tail.next = new_node
        new_node.prev = tail

    return llist
