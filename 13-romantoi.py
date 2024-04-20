class Solution:
    def romanToInt(self, s):
        roman_n = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total = 0
        last_vis = 0

        for alg in reversed(s):
            if last_vis > roman_n.get(alg):
                total -= roman_n.get(alg)
            else:
                total += roman_n.get(alg)
                
            last_vis = roman_n.get(alg)

        return total

solution_instance = Solution()

print(solution_instance.romanToInt("MCMXCIV"))
