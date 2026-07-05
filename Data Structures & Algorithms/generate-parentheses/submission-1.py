class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def dfs(left, right, curr):
            if left == n and right == n:
                result.append(''.join(curr))
                return

            # close
            if left > right:
                dfs(left, right + 1, curr + [')'])

            # open a new one
            if left < n:
                dfs(left + 1, right, curr + ['('])
        
        dfs(0, 0, [])
        return result
            

        