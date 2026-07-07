class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        count = 0
        j = 0
        for i in range(len(s)):
            while j < len(t):
                if s[i] != t[j]:
                    j += 1
                else:
                    count += 1
                    j += 1
                    break
            else:
                return False

        return count == len(s)

                    
                