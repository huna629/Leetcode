class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            find = target-nums[i]
            if find in hashmap:
                return [i, hashmap[find]]
            hashmap[nums[i]]=i
        