# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            left = self.rec(root.left)
            right = self.rec(root.right)
            ans = max(left,right) + 1
            
            return ans

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.rec(root)

    
        