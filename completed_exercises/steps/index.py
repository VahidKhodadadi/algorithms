def steps(n, row = 0, stair = ""):
    if row == n:
        return
    if len(stair) == n:
        print(stair)
        steps(n, row + 1)
        return
        
    add = None
    if len(stair) <= row:
        add = "#"
    else:
        add = " "
    steps(n, row, stair + add)