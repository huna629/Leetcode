from collections import Counter

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i]=1
        curr= 0
        
        for key in sorted(dic.keys()):
            print(key)
            if curr!=key:
                return curr
            curr+=1
        return len(nums)