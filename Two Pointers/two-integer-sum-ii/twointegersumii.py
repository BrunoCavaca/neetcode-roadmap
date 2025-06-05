class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        minPointer = 0
        maxPointer = len(numbers) - 1
        currentNum = numbers[minPointer] + numbers[maxPointer] 
        while currentNum != target:
            if currentNum > target:
                maxPointer -= 1
            else:
                minPointer += 1
            currentNum = numbers[minPointer] + numbers[maxPointer]

        return [minPointer + 1,maxPointer + 1]
        