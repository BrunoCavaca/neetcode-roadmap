class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = nums[0]
        prefixArr = [1] * n
        for i in range(n):
            if i == 0:
                prefixArr[i] = 1 * nums[i]
            else:
                prefix *= nums[i]
                prefixArr[i] = prefix
        
        
        postfix = nums[n - 1]
        postfixArr = [1] * n
        for i in range(n - 1,-1,-1):
            if i == n - 1:
                postfixArr[i] = postfix 
            else:
                postfix *= nums[i]
                postfixArr[i] = postfix    
        final = [1] * n
        for i in range(n):
            if i == 0:
                final[i] = (postfixArr[i + 1])
            elif i == n - 1:
                final[i] = prefixArr[i - 1]
            else:
                final[i] = prefixArr[i - 1] * postfixArr[i + 1]
        print(prefixArr, postfixArr)
        return final