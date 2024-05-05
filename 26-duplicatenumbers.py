class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer = 1
        for num in nums[1:]:
            print(nums[pointer], num)
            if num > nums[pointer - 1]:
                nums[pointer] = num
                pointer += 1
            
            print(nums)
        return pointer


    
solution_instance = Solution()

print(solution_instance.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))