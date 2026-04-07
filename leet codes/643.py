class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        _max = sum(nums[0:k])
        window_sum = _max
        left = 0

        for right in range(k, len(nums)):
            window_sum = window_sum - nums[left] + nums[right]
            if window_sum > _max:
                _max = window_sum
            left+=1 

        return round(_max/k, 5)
