import math

def pyramid(n, row = 0, stair = ""):
    if row == n:
        return
    if len(stair) == (n * 2) - 1:
        print(stair)
        pyramid(n, row + 1)
        return
        
    add = None
    if abs(math.floor(((n * 2) - 1) / 2) - len(stair)) <= row:
        add = "#"
    else:
        add = " "
    pyramid(n, row, stair + add)