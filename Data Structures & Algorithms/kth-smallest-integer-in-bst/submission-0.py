# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = k
        ans = None

        def inorder(root: Optional[TreeNode]) -> int:
            nonlocal cur, ans
            if root == None or ans != None:
                return ans

        
            inorder(root.left)
            cur -= 1 
            if cur == 0:
                ans = root.val
                return ans
            inorder(root.right)
        
        inorder(root)
        return ans