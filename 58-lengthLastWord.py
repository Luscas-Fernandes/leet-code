class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordSize = 0
        s = s.strip()
        for i in s[::-1]:
            if i == " ":
                break
            wordSize += 1

        return wordSize