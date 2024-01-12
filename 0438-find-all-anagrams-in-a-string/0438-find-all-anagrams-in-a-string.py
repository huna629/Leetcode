class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)==0 or len(p)==0 or len(s)<len(p): return []
        ns, np = len(s), len(p)
        cnt_p = Counter(p)
        cnt_s = Counter()
        ans = []
        curr = ""
        for i in range(len(s)):
            cnt_s[s[i]]+=1
            
            if i>=np:
                if cnt_s[s[i-np]]==1: 
                    del cnt_s[s[i-np]]
                else:
                    cnt_s[s[i-np]]-=1
            
            if cnt_p==cnt_s:
                ans.append(i-np+1)
        return ans