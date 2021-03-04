class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        return [each for each in nums1 if each in nums2]
