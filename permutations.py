def createPerms(self, array, i, result):
    array=array.copy()
    if i==len(array)-1:
        result.append(array)
        return
  
    for j in range(i, len(array)):
        array[i], array[j]=array[j], array[i]
        self.createPerms(array, i+1, result)
        array[j], array[i]=array[i], array[j]