class Solution:
    def romanToInt(self, s: str) -> int:
        romStr = s[::-1]
        equivalent = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}
        previous = ""
        runSum = 0
        for i in range(len(s)):
            if romStr[i] == "I" and (previous == "V" or previous == "X"):
                runSum -= 1
            elif romStr[i] == "X" and (previous == "L" or previous == "C"):
                runSum -= 10
            elif romStr[i] == "C" and (previous == "D" or previous == "M"):
                runSum -= 100
            else:
                runSum += equivalent[romStr[i]]
            previous = romStr[i]
        return runSum
        
        