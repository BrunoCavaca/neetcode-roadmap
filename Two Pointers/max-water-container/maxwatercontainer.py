class Solution:
    def maxArea(self, heights: List[int]) -> int:
        minPointer = 0
        maxPointer = len(heights) - 1
        maxArea = min(heights[minPointer], heights[maxPointer]) * (maxPointer - minPointer)
        for _ in range(len(heights)):
            if heights[minPointer] < heights[maxPointer]:
                minPointer += 1
            elif heights[maxPointer] < heights[minPointer]:
                maxPointer -= 1
            else:
                maxPointer -= 1

            area = min(heights[minPointer], heights[maxPointer]) * (maxPointer - minPointer)
            if area > maxArea:
                maxArea = area
        return maxArea