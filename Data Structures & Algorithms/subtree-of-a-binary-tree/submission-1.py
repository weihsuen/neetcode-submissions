# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def traversetree(self,  root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        left = self.traversetree(root.left, subRoot)
        right = self.traversetree(root.right, subRoot)

        if root.val == subRoot.val:
            if self.checkifsame(root, subRoot):
                return True
        
        return left or right

    def checkifsame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot!=None:
            return False
        elif subRoot == None and root!=None:
            return False
        elif root == None and subRoot==None:
            return True

        left = self.checkifsame(root.left, subRoot.left)
        if left == False:
            return False
        right = self.checkifsame(root.right, subRoot.right)
        if right == False:
            return False

        if root.val != subRoot.val:
            return False
        else:
            return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.traversetree(root, subRoot)