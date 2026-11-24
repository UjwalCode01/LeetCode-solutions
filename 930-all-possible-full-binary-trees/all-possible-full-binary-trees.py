class Solution(object):
    def allPossibleFBT(self, n):
        memo = {0: [], 1: [TreeNode(0)]}

        def build(k):
            if k in memo:
                return memo[k]
            if k % 2 == 0:
                memo[k] = []
                return []

            trees = []
            for left_count in range(1, k, 2):
                right_count = k - 1 - left_count
                for left_tree in build(left_count):
                    for right_tree in build(right_count):
                        trees.append(TreeNode(0, left_tree, right_tree))

            memo[k] = trees
            return trees

        return build(n)