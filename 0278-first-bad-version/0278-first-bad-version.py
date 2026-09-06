class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n
        
        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid  # First bad version is mid or somewhere before mid
            else:
                low = mid + 1  # First bad version must be after mid
                
        return low