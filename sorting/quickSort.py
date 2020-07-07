# quicksort with modification that not random pivot is taken, but always first item in array
def quickSort(array):
    recurse(array, 0, len(array)-1)
def recurse(array, start, end):
    if start-end==1:
        return
    pivot,left,right=start,start+1,end
    while left<=right:
        if array[left]>array[pivot] and array[right]<array[pivot]:
            array[left], array[right]=array[right], array[left]
            left+=1
            right-=1
        if array[left]<=array[pivot]:
            left+=1
        if array[right]>=array[pivot]:
            right-=1
    array[pivot], array[right]=array[right],array[pivot]
    if right-start<end-right:
        recurse(array, start, right-1)
        recurse(array, right+1, end)
    else:
        recurse(array, right+1, end)
        recurse(array,start, right-1)

    
