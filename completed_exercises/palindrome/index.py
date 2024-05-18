import math

def palindrome(str):
    is_palindrome = True
    for i in range(0, math.ceil(len(str) / 2)):
        if str[i] != str[len(str) - 1 - i]:
            is_palindrome = False
            break
    return is_palindrome