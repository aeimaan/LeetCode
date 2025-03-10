class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        
        stack = []

        for c in s:
            if c in {"(", "{", "["}:
                stack.append(c)
            if len(stack) == 0: return False
            if c == ")": 
                if stack.pop() != "(": return False 
            if c == "}": 
                if stack.pop() != "{":
                    return False 
            if c == "]": 
                if stack.pop() != "[":
                    return False 

        if len(stack) != 0:
            return False 
        else:
             return True

