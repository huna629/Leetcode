# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []                            
        dic = defaultdict()                     
        maxi = 0                            
        
        def find(root):
            
            if not root:                    
                return
            
            if root.val in dic:            
                dic[root.val] += 1
            else:
                dic[root.val] = 1          
            find(root.left)
            find(root.right)
            return 
     
        find(root)
        dicval_list = list(dic.values())   
        maxi = max(dicval_list)             
        for key, value in dic.items():
            if value == maxi:               
                lst.append(key)
        return lst