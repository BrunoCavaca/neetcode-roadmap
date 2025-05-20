class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = {}
        for i in (nums):
            ls[i] = ls.get(i,0) + 1
            if ls.get(i)> 1:
                return True
        return False

