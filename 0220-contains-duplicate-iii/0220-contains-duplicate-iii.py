class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False
        
        buckets = {}
        w = valueDiff + 1
        
        for i, num in enumerate(nums):
            # Compute bucket ID
            bucket_id = num // w
            
            # Case 1: Check if same bucket has a value
            if bucket_id in buckets:
                return True
            
            # Case 2: Check adjacent left bucket
            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
                
            # Case 3: Check adjacent right bucket
            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Insert current element into its bucket
            buckets[bucket_id] = num
            
            # Maintain sliding window of size indexDiff
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]
                
        return False