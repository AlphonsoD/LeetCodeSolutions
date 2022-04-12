class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b, carry, pointer, result = list(a)[::-1], list(b)[::-1], 0, 0, ""
        
        while pointer <= min(len(a)-1, len(b)-1):
            sum = int(a[pointer]) + int(b[pointer]) + carry
            if sum == 0 or sum == 1:
                result, carry = str(sum) + result, 0
            else:
                result, carry = str(sum % 2) + result, 1
            pointer += 1
        
        if len(a) > len(b):
            while pointer < len(a):
                sum = int(a[pointer]) + carry
                if sum == 0 or sum == 1:
                    result, carry = str(sum) + result, 0
                else:
                    result, carry = "0" + result, 1
                pointer += 1
                
        else:
            while pointer < len(b):
                sum = int(b[pointer]) + carry
                if sum == 0 or sum == 1:
                    result, carry = str(sum) + result, 0
                else:
                    result, carry = "0" + result, 1
                pointer += 1
                
        if carry == 1:
            result = "1" + result
            
        return result
        