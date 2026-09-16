import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        counts = collections.defaultdict(int)

        def get_subtree_sum(node):
            if not node:
                return 0
            
            # Post-order traversal: compute sum of left and right subtrees
            left_sum = get_subtree_sum(node.left)
            right_sum = get_subtree_sum(node.right)
            
            total_sum = node.val + left_sum + right_sum
            counts[total_sum] += 1
            
            return total_sum

        get_subtree_sum(root)
        
        # Find maximum frequency and return all sums matching that frequency
        max_freq = max(counts.values())
        return [s for s, freq in counts.items() if freq == max_freq]