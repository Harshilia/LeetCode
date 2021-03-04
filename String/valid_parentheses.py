from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        # if s=='':
        #     return True
        # stack = deque()
        # for each in s:
        #     if each=='(' or each=='{' or each=='[':
        #         stack.append(each)
        #     else:
        #         if stack:
        #             top = stack.pop()
        #             if each==')' and top=='(':continue
        #             elif each=='}' and top=='{':continue
        #             elif each==']' and top=='[':continue
        #             else:return False
        #         else:return False
        # if stack:return False
        # else:return True

        # Efficient Solution
        stack = []
        dictionary = {')':'(',']':'[','}':'{'}

        for each in s:
            if each in dictionary.values():
                stack.append(each)
            else:
                if stack:
                    if stack.pop() != dictionary[each]:
                        return False
                else:
                    return False
        if stack:return False
        else:return True
