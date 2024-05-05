class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
    
solution_instance = Solution()

solution_instance.removeElement([3,2,2,3], 2)