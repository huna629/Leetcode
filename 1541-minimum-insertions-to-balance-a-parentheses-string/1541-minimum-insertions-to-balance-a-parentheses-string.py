class Solution:
    def minInsertions(self, s: str) -> int:
        res, right = 0, 0
        for c in s:
            if c=='(':
                if right%2:
                    res+=1
                    right-=1
                right+=2
            else:
                right-=1
                if right<0:
                    right+=2
                    res+=1
        return res+right
                