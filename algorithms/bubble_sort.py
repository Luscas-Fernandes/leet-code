def bubble(nums):
    size = len(nums)

    for _ in nums:
        isSorted = 1
        print(nums)
        for i in range(size - 1):
            if nums[i] > nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
                isSorted = 0
            
        if isSorted:
            break

    return nums


array = [2,4,5,3,1]

print(bubble(array))
