"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        old_to_new = {}

        def dfs(curr_node):
            # If node already cloned, return the cloned instance
            if curr_node in old_to_new:
                return old_to_new[curr_node]

            # Create new clone and add to hash map
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy

            # Recursively clone all neighbors
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)