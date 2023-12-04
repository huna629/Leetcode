class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            if nums[i]<=prev:
                prev+=1
                ans += prev-nums[i]
            else:
                prev = nums[i]
        return ans