# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        def getHeight(node):
            if not node:
                return -1
            
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            currentHeight = max(leftHeight, rightHeight) + 1

            nonlocal result
            if len(result) == currentHeight:
                result.append([])
            result[currentHeight].append(node.val)

            return currentHeight
        
        getHeight(root)

        return result