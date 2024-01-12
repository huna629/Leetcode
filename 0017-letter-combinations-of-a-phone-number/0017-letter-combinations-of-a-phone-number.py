class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="": return []
        dic = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g','h', 'i'], '5':['j','k','l'], '6':['m','n','o'], 
            '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y','z']}
        
        
        
        def backtrack(index, path):
            if index==len(digits):
                ans.append("".join(path))
                return
            for char in dic[digits[index]]:
                backtrack(index+1, path+[char])
        ans = []        
        backtrack(0, [])       
        return ans