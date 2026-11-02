class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        # natural: current index par swap na karne par total swaps
        # swapped: current index par swap karne par total swaps
        natural, swapped = 0, 1
        
        for i in range(1, n):
            new_natural = float('inf')
            new_swapped = float('inf')
            
            # Case 1: Agar bina cross-swap ke sequence already increasing hai
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                new_natural = min(new_natural, natural)
                new_swapped = min(new_swapped, swapped + 1)
                
            # Case 2: Agar cross-swap karne par sequence increasing ho jati hai
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                new_natural = min(new_natural, swapped)
                new_swapped = min(new_swapped, natural + 1)
                
            natural, swapped = new_natural, new_swapped
            
        return min(natural, swapped)