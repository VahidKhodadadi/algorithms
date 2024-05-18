def vowels(str):
    count = 0
    checker = ['a', 'e', 'i', 'o', 'u']
    for char in str:
        if char in checker:
            count += 1
    return count