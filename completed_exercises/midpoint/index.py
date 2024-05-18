def midpoint(list):
    slow = list.getFirst()
    fast = list.getFirst()

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow