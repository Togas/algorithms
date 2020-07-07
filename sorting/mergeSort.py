# standard mergeSort, that returns sorted copy of original array and with space compleexity =(n log(n))
def mergeSort(array):
    if len(array) == 1:
        return array
    middle = len(array)>>1
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



# advanced mergeSort, that sorts in place with space O(n)
def mergeSortInPlace(array):
    mergeSortHelper(array, array.copy(), 0, len(array)-1)
    return array

def mergeSortHelper(array1, array2, left, right):
    if left==right:
        return 
    middle=(left+right)>>1
    mergeSortHelper(array2, array1, left, middle)
    mergeSortHelper(array2, array1, middle+1, right)
    mergeHelper(array1, array2, left, middle, middle+1, right)

def mergeHelper(array, array2, left1, right1, left2, right2):
    i=left1
    while left1<=right1 and left2<=right2:
        if array2[left1]<=array2[left2]:
            array[i]=array2[left1]
            left1+=1
        else:
            array[i]=array2[left2]
            left2+=1
        i+=1
    while left1<=right1:
        array[i]=array2[left1]
        left1+=1
        i+=1
    while left2<=right2:
        array[i]=array2[left2]
        left2+=1
        i+=1
