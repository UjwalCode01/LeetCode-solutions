class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # 1. Dono arrays ko aapas mein jodna (merge)
        merged = nums1 + nums2
        
        # 2. Pure array ko line se lagana (sort)
        merged.sort()
        
        n = len(merged)
        
        # 3. Agar total numbers ODD (visham) hain, toh beech wala number median hoga
        if n % 2 != 0:
            return float(merged[n // 2])
        # 4. Agar total numbers EVEN (sam) hain, toh beech ke do numbers ka average median hoga
        else:
            mid1 = merged[n // 2]
            mid2 = merged[(n // 2) - 1]
            return float(mid1 + mid2) / 2.0