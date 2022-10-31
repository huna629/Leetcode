# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = set()
        
        if not root:
            return False
        
        def dfs(node):
            if node:
                val.add(node.val)
                dfs(node.left)
                dfs(node.right)
            
        dfs(root)
        return len(val)==1