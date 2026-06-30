class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depthFromNode(currentNode: Optional[TreeNode]) -> int:
            if not currentNode: 
                return 0
            return 1 + max(depthFromNode(currentNode.left), depthFromNode(currentNode.right))

        def maxDiameter(root: Optional[TreeNode]) -> int:
            if not root: 
                return 0
            
            current_diameter = depthFromNode(root.left) + depthFromNode(root.right)
            return max(current_diameter, maxDiameter(root.left), maxDiameter(root.right))
        
        return maxDiameter(root)