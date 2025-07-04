from BinarySearchTree import Node


def insert(self, val):
    new_node = Node(val)

    if self.root is None:
        self.root = new_node
        return

    inserted = False
    current = self.root

    while not inserted:
        if current.info > val:
            if current.left:
                current = current.left
            else:
                current.left = new_node
                inserted = True
        else:
            if current.right:
                current = current.right
            else:
                current.right = Node(val)
                inserted = True
