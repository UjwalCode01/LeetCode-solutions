from collections import defaultdict


class Solution(object):

  def numberOfBoomerangs(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    total_boomerangs = 0

    for p1 in points:
      dist_counts = defaultdict(int)

      for p2 in points:
        # Calculate squared Euclidean distance to avoid floating-point issues
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        dist = dx * dx + dy * dy

        dist_counts[dist] += 1

      # Calculate permutations for each distance group: k * (k - 1)
      for count in dist_counts.values():
        total_boomerangs += count * (count - 1)

    return total_boomerangs