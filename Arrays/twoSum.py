class Solution:
    def twoSum(self, nums, target):
        if len(nums) == 2:
            return [0,1]

        valDict = {}

        for index,value in enumerate(nums):
            difference = target - value
            if difference in valDict:
                return [valDict[difference],index]
            valDict[value] = index
