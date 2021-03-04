class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        for each in num:
            
            while k and stack and stack[-1]>each:
                stack.pop()
                k -= 1
            stack.append(each)
        
        while k>0:
            stack.pop()
            k -= 1
        
        # Remove leading zeros
        output = "".join(stack).lstrip("0")
        
        return (output if output else "0")
        