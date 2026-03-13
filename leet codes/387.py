class Solution:
    def firstUniqChar(self, s: str) -> int:
        _dic = {}

        for idx, i in enumerate(s):
            if not _dic.get(i):
                _dic[i] = [idx, 1]
            else:
                _dic[i][1] += 1

        for i in s:
            if _dic[i][1] == 1:
                return _dic[i][0]

        return -1 
    
s = Solution()

sol = s.firstUniqChar("aabb")
print(sol)