import numpy as np
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maximum = 0
        for i,each in enumerate(nums):
            if i>maximum:return False
            maximum = max(maximum,i+each)
            if maximum == len(nums)-1:return True
        return True
