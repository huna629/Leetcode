class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 
        if len(nums)==1:
            return nums[0]

        currSum = maxSum = nums[0]
        i = 1
        while i<len(nums):
            currSum=max(currSum+nums[i], nums[i])
            maxSum =max(maxSum, currSum)
            i+=1

        return maxSum
