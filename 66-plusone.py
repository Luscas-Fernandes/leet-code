class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        def checkSum(digits, i):
            if i == 0 and digits[i] + 1 == 10:
                digits[i] = 0
                digits.insert(0, 1)
            elif digits[i] + 1 == 10:
                digits[i] = 0
                checkSum(digits, i - 1)
            else:
                digits[i] += 1

            return digits

        if not digits:
            return []
        
        new_digits = checkSum(digits, len(digits) - 1)

        return new_digits
