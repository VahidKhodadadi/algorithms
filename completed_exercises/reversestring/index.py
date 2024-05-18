def reverse(str):
    reversed = ''
    for char in str:
        reversed = char + reversed
    return reversed