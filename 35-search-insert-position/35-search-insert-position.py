class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        beg = 0
        end= N-1
        result=-1
        while(beg<=end):
            mid = int((beg+end)/2)
            if nums[mid]<target:
                beg=mid+1
            elif nums[mid]>target :
                end=mid-1
                ##result=mid
            else:
                return mid
            
        return beg