#sort in place
def insertionSort(array):
  for i in range(1,len(array)):
    j=i-1
    while j>=0:
      if array[i]<array[j]:
        array[i], array[j]=array[j], array[i]
        j-=1
        i-=1
      else:
        break