# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # If root itself ==  p or q, and the other found in its left or right child, return root
        # If find one in root.left, find another in root.right, return root

        def dfs(curr):
            if not curr:
                return None
            if curr.val == p.val or curr.val == q.val:
                return curr
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left and right:
                return curr

            return left if left else right            
        
        return dfs(root)


        
        