# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        l = 0 
        r = len(inorder) -1
        i = 0 
        index_map = {val: idx for idx, val in enumerate(inorder)}

        def recur(l:int, r:int):
            nonlocal i
            if l > r:
                return None
            root = TreeNode(preorder[i], None, None)

            mid = index_map[preorder[i]]
            i +=1
            root.left = recur(l,mid -1)
            root.right = recur(mid +1, r)
            return root
        
        return recur(0,r)

        