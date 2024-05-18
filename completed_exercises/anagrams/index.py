import re

def cleanString(str):
    cleanedStr = re.sub("/[^\w]/g", '', str).replace(" ", "").lower()
    cleanedArr = list(cleanedStr)
    cleanedArr.sort()
    sortedCleanedStr = "".join(cleanedArr)
    return sortedCleanedStr

def anagrams(stringA, stringB):
    return cleanString(stringA) == cleanString(stringB)