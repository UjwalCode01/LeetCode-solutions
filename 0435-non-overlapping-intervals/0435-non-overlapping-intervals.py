class Solution(object):

  def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if not intervals:
      return 0

    # Sort intervals based on their end time
    intervals.sort(key=lambda x: x[1])

    removals = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
      start, end = intervals[i]

      # If current interval overlaps with the previous chosen interval
      if start < prev_end:
        removals += 1
      else:
        # No overlap, update end time to current interval's end
        prev_end = end

    return removals