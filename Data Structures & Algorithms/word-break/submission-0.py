class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def helper(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                word_length = len(word)
                end = i + word_length
                if end <= len(s) and s[i : end] == word:
                    if helper(end):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
            
        return helper(0)