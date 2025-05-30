class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for number in nums:
            if (number - 1) not in numSet:
                length = 0
                while (number + length) in numSet:
                    length += 1

                if length > longestSequence:
                    longestSequence = length
        
        return longestSequence