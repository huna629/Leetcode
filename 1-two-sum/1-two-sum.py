class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=i
        
        for j in range(len(nums)-1):
            currTarget=target-nums[j]
            if currTarget in dict.keys() and dict.get(currTarget)!=j:
                return [j, dict.get(currTarget)]
            