def fromLast(list, n):
    slow = list.getFirst()
    fast = list.getFirst()

    while (n > 0):
        fast = fast.next
        n -= 1

    while (fast.next):
        slow = slow.next
        fast = fast.next

    return slow