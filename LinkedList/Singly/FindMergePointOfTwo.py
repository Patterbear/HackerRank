def findMergeNode(head1, head2):
    pointer1 = head1
    pointer2 = head2

    while pointer1 != pointer2:
        if pointer1:
            pointer1 = pointer1.next
        else:
            pointer1 = head2

        if pointer2:
            pointer2 = pointer2.next
        else:
            pointer2 = head1

    return pointer1.data
