class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 1
        bitsCounts = 0
        
        while bits < n:
            if bits & n:
                bitsCounts += 1
            
            bits *= 2

        if bits & n:
                bitsCounts += 1
                bits *= 2
            
        return bitsCounts