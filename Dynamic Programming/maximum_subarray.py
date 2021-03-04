class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum, output = 0,float('-inf')
        for each in nums:
            max_sum = max(each, max_sum+each)
            output = max(output, max_sum)
        return output