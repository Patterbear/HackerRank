from LinkedList import SinglyLinkedListNode


def insertNodeAtPosition(llist, data, position):
    index = 0
    current = llist

    while index != position - 1:
        current = current.next
        index += 1

    temp = current.next
    new_node = SinglyLinkedListNode(data)
    current.next = new_node
    new_node.next = temp

    return llist
