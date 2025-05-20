class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letterDict = {}
        for letter in s:
            letterDict[letter] = letterDict.get(letter,0) + 1
        
        for letter in t:
            val = letterDict.get(letter,0)
            if val == 0 :
                return False
            else:
                letterDict[letter] = letterDict.get(letter) - 1
        
        return not sum(letterDict.values()) >= 1 
