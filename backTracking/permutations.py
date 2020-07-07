def createPerms(array, i, result):
    if i==len(array)-1:
        result.append(array.copy())
        return result
    for j in range(i, len(array)):
        array[i], array[j]=array[j], array[i]
        createPerms(array, i+1, result)
        array[j], array[i]=array[i], array[j]
    return result