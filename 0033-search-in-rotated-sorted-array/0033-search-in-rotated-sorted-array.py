class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<=1:
            if nums[0]==target:
                return 0
            else:
                return -1
            
        start = nums.index(min(nums))
        print(start)
        arr=[]
        if start!=0:
            arr = nums[start:]+nums[0:start]
        else:
            arr =nums
        print(arr)
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]==target:
                return (start+mid)%len(nums)
            if arr[mid]>target:
                high = mid-1
            else:
                low=mid+1
        return -1