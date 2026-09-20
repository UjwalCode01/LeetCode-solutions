class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Map each unique bitmask to the maximum word length with that mask
        mask_to_len = {}
        
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            
            # Store the maximum length for this specific bitmask
            mask_to_len[mask] = max(mask_to_len.get(mask, 0), len(word))
        
        max_product = 0
        
        # Compare pairs of bitmasks
        masks = list(mask_to_len.keys())
        n = len(masks)
        
        for i in range(n):
            for j in range(i + 1, n):
                # If masks don't share any common characters
                if (masks[i] & masks[j]) == 0:
                    product = mask_to_len[masks[i]] * mask_to_len[masks[j]]
                    max_product = max(max_product, product)
                    
        return max_product