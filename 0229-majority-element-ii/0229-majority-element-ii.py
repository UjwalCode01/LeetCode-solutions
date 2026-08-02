class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # Step 1: Find 2 potential candidates
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
                
        # Step 2: Verify frequency of candidates
        result = []
        n = len(nums)
        
        if cand1 is not None and nums.count(cand1) > n // 3:
            result.append(cand1)
        if cand2 is not None and cand2 != cand1 and nums.count(cand2) > n // 3:
            result.append(cand2)
            
        return result