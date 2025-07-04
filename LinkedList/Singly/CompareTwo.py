def compare_lists(llist1, llist2):
    if not llist1 and not llist2:
        return 1
    if not llist1 or not llist2:
        return 0
    if llist1.data != llist2.data:
        return 0

    return compare_lists(llist1.next, llist2.next)
