class Solution:
    def isPalindrome(self, x):
        original_number = str(x)
        reversed_number = str(x)[::-1]

        if original_number == reversed_number:
            return True
        
        return False


solution_instance = Solution()

print(solution_instance.isPalindrome(101))
