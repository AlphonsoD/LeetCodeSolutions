class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + carry > 9:
                digits[i], carry = 0, 1
            else:
                digits[i], carry = digits[i] + carry, 0
        if carry > 0:
            digits.insert(0, carry)
        return digits
            