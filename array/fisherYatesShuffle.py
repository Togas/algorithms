import random
# also called Knuth-shuffle. Sorts array in O(n) time, =0(1) space and in place
def shuffle(array):
    for i in range(len(array)):
        j=random.randint(i, len(array)-1)
        array[i], array[j]=array[j], array[i]
    return array
    