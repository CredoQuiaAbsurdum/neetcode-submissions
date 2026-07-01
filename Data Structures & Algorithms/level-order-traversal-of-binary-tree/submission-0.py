# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def helper(root, depth):

            if not root:
                return

            nonlocal result
            if len(result) == depth:
                result.append([])
            
            result[depth].append(root.val)

            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        
        helper(root, 0)

        return result



