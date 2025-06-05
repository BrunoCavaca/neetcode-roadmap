class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i,v in enumerate(nums):
            if v > 0:
                break
            
            if i > 0 and v == nums[i-1]:
                continue

            minPointer = i + 1
            maxPointer = len(nums) - 1
            while minPointer < maxPointer:
                tempVal = nums[i] + nums[minPointer] + nums[maxPointer]
                if tempVal < 0:
                    minPointer += 1
                elif tempVal > 0:
                    maxPointer -= 1
                else:
                    result.append([nums[i],nums[minPointer],nums[maxPointer]])
                    minPointer += 1
                    maxPointer -= 1
                    while nums[minPointer] == nums[minPointer - 1] and minPointer < maxPointer:
                        minPointer += 1

        return result
