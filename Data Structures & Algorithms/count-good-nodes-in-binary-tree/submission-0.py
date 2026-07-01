# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0

        def dfs(node, great):
            if not node:
                return
            if great <= node.val:
                nonlocal count
                count += 1
                great = node.val
            dfs(node.left, great)
            dfs(node.right, great)
        
        dfs(root, root.val)
        return count
        