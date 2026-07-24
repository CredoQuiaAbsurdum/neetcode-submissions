class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []

        combination = []

        def helper(i):
            if len(combination) == k:
                result.append(combination.copy())
                return
            elif i >= n:
                return
            
            combination.append(i + 1)
            helper(i + 1)
            combination.pop()
            helper(i + 1)

        helper(0)

        return result
