
def createSubsets(nums):
    subsets=[]
    recurse(0, nums, [], subsets)
    return subsets

def recurse(index, nums, current, subsets):
    subsets.append(current.copy())
    for i in range(index, len(nums)):
        current.append(nums[i])
        recurse(i+1,nums, current, subsets)
        current.pop()
print(createSubsets([1,2,3,4]))
