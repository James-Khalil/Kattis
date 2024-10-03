class Solution:
    def longestPalindrome(self, s: str) -> str:
        currentString = ''
        result = ''
        for i in range(len(s)):
            StringQueue = ''
            stringHolder = ''
            result = ''
            workingString = s[i:]
            for char in workingString:
                stringHolder += char
                if char == StringQueue[-1]:
                    StringQueue.
                
                    if len(currentString) > len(result):
                        result = currentString
        return result

print(Solution.longestPalindrome(Solution, input()))