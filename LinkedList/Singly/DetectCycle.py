def has_cycle(head):
    visited = []
    current = head

    while current:
        if current in visited:
            return 1
        visited.append(current)
        current = current.next

    return 0
