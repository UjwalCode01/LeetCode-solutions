import bisect

class Solution:
    def maximumSumQueries(self, nums1, nums2, queries):
        # Pair elements: (nums1[j], nums2[j])
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[0], reverse=True)
        
        # Store queries with original index: (x_i, y_i, original_index)
        sorted_queries = sorted([(q[0], q[1], i) for i, q in enumerate(queries)], key=lambda x: x[0], reverse=True)
        
        ans = [-1] * len(queries)
        stack = []  # Elements stored as: (b_val, max_sum)
        
        pair_idx = 0
        n = len(pairs)
        
        for x, y, original_idx in sorted_queries:
            # Add all valid pairs satisfying nums1[j] >= x
            while pair_idx < n and pairs[pair_idx][0] >= x:
                a, b = pairs[pair_idx]
                s = a + b
                
                # Maintain monotonic stack: higher b should have higher sum
                while stack and stack[-1][1] <= s:
                    stack.pop()
                
                if not stack or stack[-1][0] < b:
                    stack.append((b, s))
                
                pair_idx += 1
            
            # Binary search for the smallest b_val >= y
            idx = bisect.bisect_left(stack, (y, -1))
            if idx < len(stack):
                ans[original_idx] = stack[idx][1]
                
        return ans
        