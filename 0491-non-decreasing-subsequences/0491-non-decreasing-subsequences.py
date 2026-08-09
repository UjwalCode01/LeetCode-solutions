class Solution(object):

  def findSubsequences(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []

    def backtrack(start_idx, current_seq):
      if len(current_seq) >= 2:
        res.append(list(current_seq))

      used_in_level = set()

      for i in range(start_idx, len(nums)):
        # Skip if duplicate element at current depth OR violates non-decreasing order
        if nums[i] in used_in_level:
          continue
        if current_seq and nums[i] < current_seq[-1]:
          continue

        used_in_level.add(nums[i])
        current_seq.append(nums[i])

        backtrack(i + 1, current_seq)

        current_seq.pop()

    backtrack(0, [])
    return res