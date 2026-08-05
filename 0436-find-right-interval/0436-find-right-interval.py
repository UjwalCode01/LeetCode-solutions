import bisect


class Solution(object):

  def findRightInterval(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[int]
    """
    # Map start values to their original indices
    starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
    start_values = [s[0] for s in starts]

    res = []

    for interval in intervals:
      end = interval[1]
      # Binary search to find smallest start >= end
      idx = bisect.bisect_left(start_values, end)

      if idx < len(starts):
        res.append(starts[idx][1])
      else:
        res.append(-1)

    return res