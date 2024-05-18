def levelWidth(root):
    arr = [root, 's']
    counters = [0]

    while (arr.length > 1):
        node = arr.pop(0)

        if node == 's':
            counters.append(0)
            arr.append('s')
        else:
            arr.extend(node.children)
            counters[counters.length - 1] += counters[counters.length - 1]

    return counters