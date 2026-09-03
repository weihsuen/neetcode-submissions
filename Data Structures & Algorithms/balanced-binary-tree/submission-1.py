# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return 0
        
        
        left = self.recur(root.left)
        if left == -1:
            return -1
        right = self.recur(root.right)
        if right == -1:
            return -1

        if abs(left-right)>1:
            return -1
        else:
            return max(left,right)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = self.recur(root)
        if ans == -1:
            return False
        else:
            return True
        
        


        