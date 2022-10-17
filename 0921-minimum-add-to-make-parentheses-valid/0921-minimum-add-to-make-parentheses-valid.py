class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
                if char == ')' and stack and stack[-1]=='(':
                    print('need to pop '+char)
                    stack.pop()
                else:
                    print('need to push '+char)
                    stack.append(char)    
                    
        return len(stack)
            
            
                