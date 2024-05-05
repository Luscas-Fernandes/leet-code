class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
solution_instance = Solution()

print(solution_instance.strStr("sadbutsad", "sad"))