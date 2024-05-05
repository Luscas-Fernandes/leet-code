class Solution:
    def isValid(self, s: str) -> bool:
        stringList = []
        vabg = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for c in s:
            if c in vabg:
                stringList.append(vabg.get(c))

            else:
                if stringList and c == stringList[-1]:
                    stringList.pop()
                else:
                    return False
            
        if not stringList:
            return True
        else:
            return False
        

solution_instance = Solution()

print(solution_instance.isValid("()"))