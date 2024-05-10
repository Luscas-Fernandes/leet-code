class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return None

        preTarget = None

        for i, num in enumerate(nums):
            print(preTarget)
            if num < target: preTarget = i

            if num == target: return i

        if preTarget is None: return 0

        return preTarget + 1 


solution_instance = Solution() # Fora do tempo o(log N) pedido

print(solution_instance.searchInsert(nums = [1,3,5,6], target = 5))
