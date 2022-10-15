class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for char in s:
            if char!='#':
                stack1.append(char)
            if char=='#' and stack1:
                stack1.pop()
            # if char=='#' and not stack1:
            #     return False;
        
        for char in t:
            if char!='#':
                stack2.append(char)
            if char=='#' and stack2:
                stack2.pop()        
            # if char=='#' and not stack2:
            #     return False;
            
        if len(stack1)!=len(stack2):
            return False
        
        while stack1 and stack2:
            if stack1.pop()!=stack2.pop():
                return False
            
        return True;