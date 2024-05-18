def maxChar(str):
    charMap = {}
    max = 0
    maximumChar = ""
    for char in str:
        if char in charMap:
            charMap[char] = charMap[char] + 1
        else:
            charMap[char] = 1
            
    for char in charMap:
        if charMap[char] > max:
            max = charMap[char]
            maximumChar = char
    
    return maximumChar