def reverse(llist):
    if not llist or not llist.next:
        return llist

    new_llist = reverse(llist.next)

    llist.next.next = llist
    llist.next = None

    return new_llist
