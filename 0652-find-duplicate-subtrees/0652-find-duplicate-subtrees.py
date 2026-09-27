# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[TreeNode]
        """
        count = defaultdict(int)
        result = []

        def serialize(node):
            if not node:
                return "#"
            
            # Post-order traversal to build serialization bottom-up
            serialized_str = "{},{},{}".format(node.val, serialize(node.left), serialize(node.right))
            
            # Increment tree representation frequency
            count[serialized_str] += 1
            
            # Add to result on the second occurrence only
            if count[serialized_str] == 2:
                result.append(node)
                
            return serialized_str

        serialize(root)
        return result