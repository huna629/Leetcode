class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        vol = 0
        while(l<r):
            w=r-l
            vol=max(vol, min(height[l], height[r])*w)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return vol
    