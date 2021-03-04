# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        minimum = float('inf')
        while start <= end:

            mid = (start + end)//2;

            check = isBadVersion(mid)

            if check == False:
                start = mid + 1

            else:
                end = mid - 1
                minimum = min(minimum, mid)
        return minimum
