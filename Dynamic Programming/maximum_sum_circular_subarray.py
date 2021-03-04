class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # def maxSum(A):
        #     max_sum, output = 0,float('-inf')
        #     for each in nums:
        #         max_sum = max(each, max_sum+each)
        #         output = max(output, max_sum)
        #     return output
        # middle = maxSum(A)
        # circular = maxSum([each*(-1) for each in A]) + sum(A)
        # return (circular if circular>middle and circular>0 else middle)
    
        total, max_sum, max_output, min_sum, min_output = 0, 0, float('-inf'), 0, float('inf')
        for each in A:
            max_sum = max(each, max_sum+each)
            max_output = max(max_output, max_sum)
            min_sum = min(each, min_sum+each)
            min_output = min(min_output, min_sum)
            total += each
        return max(max_output, total-min_output) if max_output>0 else max_output