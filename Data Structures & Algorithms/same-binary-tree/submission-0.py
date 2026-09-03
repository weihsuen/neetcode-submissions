# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def myRecur(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q != None:
            return -1
        elif q== None and p!=None:
            return -1
        elif p == None and q==None:
            return 0

        left = self.myRecur(p.left, q.left)
        if left == -1:
            return -1
        right = self.myRecur(p.right, q.right)
        if right == -1:
            return -1
        if p.val != q.val:
            return -1
        else:
            return 1
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = self.myRecur(p, q)

        if ans == -1:
            return False
        else:
            return True