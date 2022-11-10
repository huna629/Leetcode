class Solution:
    def greatestLetter(self, s: str) -> str:
        upperSet = set()
        lowerSet = set()
        for char in s:
            if char.isupper():
                upperSet.add(char.lower())
            else:
                lowerSet.add(char)
            
        ans = ''
        for char in upperSet:
            if char in lowerSet:
                if ans<char.upper():
                    ans=char.upper()
                    
        return ans