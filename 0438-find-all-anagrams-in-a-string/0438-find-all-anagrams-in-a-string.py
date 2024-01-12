class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)==0 or len(p)==0 or len(s)<len(p): return []
        cnt_p = Counter(p)
        ans = []
        for i in range(0, len(s)-len(p)+1):
            if cnt_p==Counter(s[i:i+len(p)]):
                ans.append(i)
        return ans