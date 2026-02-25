nums = [1,2,3,1]
k = 3


""" nums = [1,2,3,1,2,3]
k = 2 """ 

""" nums = [99,99]
k = 2 """

""" nums = [1,1,1,2,3,4]
k = 3 """

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    if k == 0:
        return False
    
    lPointer = 0
    numbersInWindow = {}

    for rPointer in range(len(nums)):
        if numbersInWindow.get(nums[rPointer]):
            return True        

        numbersInWindow[nums[rPointer]] = 1

        if rPointer - lPointer >= k:
            numbersInWindow[nums[lPointer]] = 0
            lPointer += 1

    return False





print(containsNearbyDuplicate(nums, k))
