# standard mergeSort, that returns sorted copy of original array
def mergeSort(array):
    if len(array) == 1:
        return array
    middle = len(array)//2
    leftArray = mergeSort(array[:middle])
    rightArray = mergeSort(array[middle:])
    return merge(leftArray, rightArray)


def merge(array1, array2):
    result = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    if i < len(array1):
        result += array1[i:]
    if j < len(array2):
        result += array2[j:]
    return result


