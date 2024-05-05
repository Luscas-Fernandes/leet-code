class Solution:
    def longestCommonPrefix(self, strs: list[str]): # rever esse 14
        if not strs:
            return ""

        lcp = ""
        strs_min_length = len(min(strs, key=len))

        for char in range(strs_min_length):
            charColumn = strs[0][char]
            for palavra in strs:
                if charColumn != palavra[char]:
                    return lcp
            lcp += charColumn

        return lcp
            
        """ 
            len(min(strs, key=len)
            corta as outras strings para o tamanho 
            da menor string (Já que é longest common PREFIX), 
            não substring
        """

solution_instance = Solution()

print(solution_instance.longestCommonPrefix(["flower","flow","flight"]))