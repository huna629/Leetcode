# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans =[]
        while queue:
            
            

                  
            l = len(queue)
            temp=[]
            for i in range(l):
                curr = queue.popleft()
                if curr:

                    if curr.left:
                        print(curr.left.val)
                        queue.append(curr.left)
                    if curr.right:
                        print(curr.right.val)
                        queue.append(curr.right) 
                temp.append(curr.val)
            ans.append(temp)
            
        return ans