class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            candidate = candidates[i]
            curr.append(candidate)
            dfs(i+1, curr, total + candidates[i])
            curr.pop()
            while(i < len(candidates)):
                i += 1
                if i >= len(candidates):
                    return
                if candidates[i] != candidate:
                    break
            dfs(i, curr, total)

        dfs(0, [], 0)

        return result