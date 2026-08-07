class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Precompute prefix XOR array
        pref = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            pref[i + 1] = pref[i] ^ arr[i]
            
        # Answer each query in O(1) time
        res = []
        for left, right in queries:
            res.append(pref[right + 1] ^ pref[left])
            
        return res