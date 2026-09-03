# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], lower: int, upper: int) -> bool:
            if root == None:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            else:
                left = right = True
                if root.left:
                    left = helper(root.left, lower, root.val)
                if root.right:
                    right = helper(root.right, root.val, upper)
                return left and right

        return helper(root, -1000, 1000)