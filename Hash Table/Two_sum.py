class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, each in enumerate(nums):
            if target-each in dictionary:
                return [dictionary[target-each], i]
            dictionary[each] = i
