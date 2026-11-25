class Solution(object):

    def subarrayBitwiseORs(self, arr):
        all_ors = set()
        curr_ors = set()
        for x in arr:
            curr_ors = {x | y for y in curr_ors} | {x}
            all_ors.update(curr_ors)
        return len(all_ors)