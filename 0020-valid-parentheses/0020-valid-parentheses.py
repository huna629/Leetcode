from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        stack = deque()
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys(): 
                if not stack or dict[char]!=stack.pop():
                    return False
            else:
                return False
        return len(stack)==0