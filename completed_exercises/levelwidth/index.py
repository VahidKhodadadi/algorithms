def levelWidth(root):
    arr = [root, 's']
    counters = [0]

    while (len(arr) > 1):
        node = arr.pop(0)

        if node == 's':
            counters.append(0)
            arr.append('s')
        else:
            arr.extend(node.children)
            counters[len(counters) - 1] += counters[len(counters) - 1]

    return counters