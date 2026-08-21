class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        oddString, evenString = "", ""
        for i in range(len(s)):
            # odd
            left, right = i, i
            
            while 0 <= left < len(s) and 0 <= right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(oddString):
                    oddString = s[left:right+1]
                left -= 1
                right += 1


            # even
            left, right = i, i + 1
            while 0 <= left < len(s) and 0 <= right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(evenString):
                    evenString = s[left:right+1]
                left -= 1
                right += 1

        if len(oddString) > len(evenString):
            return oddString
        else: 
            return evenString