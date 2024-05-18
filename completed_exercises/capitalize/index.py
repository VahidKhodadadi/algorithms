def capitalize(str):
    result = str[0].upper()
    for i in range(1, len(str)):
        if str[i - 1] == ' ':
            result += str[i].upper()
        else:
            result += str[i]
    return result