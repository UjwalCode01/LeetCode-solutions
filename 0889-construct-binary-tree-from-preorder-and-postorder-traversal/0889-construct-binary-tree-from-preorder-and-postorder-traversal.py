class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        post_idx = {val: i for i, val in enumerate(postorder)}

        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None

            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root

            left_val = preorder[pre_start + 1]
            idx = post_idx[left_val]
            left_size = idx - post_start + 1

            root.left = build(
                pre_start + 1,
                pre_start + left_size,
                post_start,
                idx
            )
            root.right = build(
                pre_start + left_size + 1,
                pre_end,
                idx + 1,
                post_end - 1
            )
            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)