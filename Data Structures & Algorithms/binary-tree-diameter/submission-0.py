# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.myMax = 0
    def myRecur(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left = self.myRecur(root.left) 
        right = self.myRecur(root.right) 
        curMax = left + right
        self.myMax = max(self.myMax, curMax)

        return max(left, right) +1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.myRecur(root)
        return self.myMax



        