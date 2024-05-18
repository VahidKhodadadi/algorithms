import math

def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

def selectionSort(arr):
    for i in range(0, len(arr)):
        indexOfMin = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[indexOfMin]:
                indexOfMin = j

        if indexOfMin != i:
            temp = arr[indexOfMin]
            arr[indexOfMin] = arr[i]
            arr[i] = temp
    return arr



def merge(left, right):
    results = []
    while (len(left) > 0 and len(right) > 0):
        if (left[0] < right[0]):
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))

    return results + left + right

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    center = math.floor(len(arr) / 2)
    left = arr[0:center]
    right = arr[center:]
    return merge(mergeSort(left), mergeSort(right))
