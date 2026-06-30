class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        result = 0

        def height(current: Optional[TreeNode]) -> int:
            if not current:
                return 0
            
            left = height(current.left)
            right = height(current.right)

            nonlocal result
            result = max(result, left + right)

            return 1 + max(left, right)
        
        height(root)
        return result