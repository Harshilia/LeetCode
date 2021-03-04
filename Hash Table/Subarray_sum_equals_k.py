from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        store_sum_dict = defaultdict(lambda : 0)
        output = 0
        current_sum = 0

        for i in range(0, len(nums)):
            current_sum += nums[i]
            if current_sum == k:
                output += 1
            if (current_sum - k) in store_sum_dict:
                output += store_sum_dict[current_sum - k]
            store_sum_dict[current_sum] += 1

        return output
