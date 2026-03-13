class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = r = 0
        _max = 0
        ocurrences = {}

        stringSize = len(s)

        ocurrences[s[0]] = 1

        while r < (stringSize - 1):
            r += 1

            if ocurrences.get(s[r]):
                ocurrences[s[r]] += 1
            else:
                ocurrences[s[r]] = 1

            while ocurrences.get(s[r]) == 3:
                ocurrences[s[l]] -= 1
                l += 1


            """ print(ocurrences)
            print([type(k) for k in ocurrences.values()]) """
            
            _max = max(sum(ocurrences.values()), _max)

        return _max


s = Solution()

_max = s.maximumLengthSubstring("eebadadbfa")
print(_max)