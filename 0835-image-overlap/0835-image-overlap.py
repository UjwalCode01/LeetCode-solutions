class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # img1 aur img2 mein jahan-jahan '1' hai, unke coordinates collect karna
        list1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        list2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Translation vectors ki frequency count karne ke liye counter
        vector_count = collections.Counter()
        
        for r1, c1 in list1:
            for r2, c2 in list2:
                # Vector calculate karna jo img1 ke point ko img2 ke point par shift kare
                vector = (r2 - r1, c2 - c1)
                vector_count[vector] += 1
                
        # Agar koi overlap nahi mila toh 0 return hoga
        return max(vector_count.values()) if vector_count else 0