# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depthFromNode(currentNode: Optional[TreeNode]) -> int:
            if not currentNode: 
                return 0
            return 1 + max(depthFromNode(currentNode.left), depthFromNode(currentNode.right))

        def rootDiameter(root: Optional[TreeNode]) -> int:
            if not root: 
                return 0
            return 1 + depthFromNode(root.left) + depthFromNode(root.right)
        
        return max(rootDiameter(root), rootDiameter(root.left), rootDiameter(root.right)) - 1
        
        
        