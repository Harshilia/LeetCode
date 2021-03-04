import collections
class Solution:
    def singleNonDuplicate(self, nums):
        # One line approach with frequency
        return collections.Counter(nums).most_common()[-1][0]
    
        # Binary Search apporach
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            mid = (left+right) // 2
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    left = mid + 2
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return nums[left]
        