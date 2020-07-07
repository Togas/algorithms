# find longest contiguous subarray
def kadanesAlgorithm(array):
    left = 0
    right = 0
    bestSum = float("-inf")
    bestArray = []
    current = 0
    for i, number in enumerate(array):
        current += number
        if current < array[i]:
            current = array[i]
            left = i
            right = i
        else:
            right += 1
        if current > bestSum:
            bestSum = current
            bestArray = array[left:right+1]
    return bestArray
