def reverse_int(n):
    str_number = str(n)
    reversed = ''
    for char in str_number:
        reversed = char + reversed
    reversed_num = None
    if n < 0:
        reversed_num = -1 * int(reversed[:-1])
    else:
        reversed_num = int(reversed)
    return reversed_num