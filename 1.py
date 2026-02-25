class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        _dic = {}
        _dic[nums[0]] = 0 # all inputs have exactly one solution with two elements.

        for idx, i in enumerate(nums[1:]):
            if target - i in _dic:
                return [_dic.get(target - i), idx + 1]
            
            _dic[i] = idx + 1


s = Solution()

sol = s.twoSum([2,7,11,15], 9)
print(sol)
