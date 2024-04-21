class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

solution_instance = Solution()

print(solution_instance.isPalindrome(101))
