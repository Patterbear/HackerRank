def reversePrint(llist):
    if llist:
        reversePrint(llist.next)
        print(llist.data)
