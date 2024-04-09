class Solution:
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        
        return False


solution_instance = Solution()

print(solution_instance.isPalindrome(101))
