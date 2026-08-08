class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['[', '{', '(']:
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if (c == ']' and last != '[') or (c == ')' and last != '(' or (c == '}' and last != '{')) :
                    return False
        
        if not stack:
            return True
        return False