# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self, root: TreeNode, curMax) -> int:
        if root == None:
            return 0
        
        good = False
        if root.val>=curMax:
            curMax = root.val
            good = True

        left = self.recur(root.left, curMax)
        right = self.recur(root.right,curMax)

        if good == True:
            return left + right + 1
        else:
            return left + right

    def goodNodes(self, root: TreeNode) -> int:
        return self.recur(root, -100)


        