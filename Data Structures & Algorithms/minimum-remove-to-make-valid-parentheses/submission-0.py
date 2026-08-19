class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        count = 0
        result = ""

        for c in s:
            if c == ')':
                if count > 0:
                    count -= 1
                    result += c
            elif c == '(':
                count += 1
                result += c
            else:
                result += c            
        
        temp = ""
        for c in reversed(result):            
            if c == '(' and count != 0:
                count -= 1
            else:
                temp += c
        result = temp[::-1] 

        return result
