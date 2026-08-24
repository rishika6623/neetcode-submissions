# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs_match(root, subRoot):
            if not subRoot and not root:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False
            else:
                return dfs_match(root.right, subRoot.right) and dfs_match(root.left, subRoot.left)
        
        if not subRoot and not root:
            return True
        elif not root or not subRoot:
            return False
        elif root.val == subRoot.val:
            return dfs_match(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        
        