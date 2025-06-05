class Solution:
    def isPalindrome(self, s: str) -> bool:
        noWhitespace = "".join(char for char in s if char.isalnum()).lower()
        startPointer = 0
        endPointer = len(noWhitespace) - 1
        while startPointer < endPointer:
            if noWhitespace[startPointer] != noWhitespace[endPointer]:
                return False
            startPointer += 1
            endPointer -= 1
        return True
        