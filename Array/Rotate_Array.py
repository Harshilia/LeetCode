class Solution:

    def reverse_array(self, array, start, end):
        while start < end:
            temp = array[start]
            array[start] = array[end]
            array[end] = temp
            start = start + 1
            end = end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1

        if k > len(nums):
            rotate = k % len(nums)
            k = rotate

        self.reverse_array(nums, n - k + 1, n)
        self.reverse_array(nums, 0, n - k)
        self.reverse_array(nums, 0, n)
