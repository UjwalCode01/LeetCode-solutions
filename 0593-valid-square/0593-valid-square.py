class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist_sq(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2

        points = [p1, p2, p3, p4]
        distances = set()

        for i in range(4):
            for j in range(i + 1, 4):
                d = dist_sq(points[i], points[j])
                if d == 0:
                    return False  # Overlapping points
                distances.add(d)

        # A valid square must have exactly 2 unique distances (sides and diagonals)
        return len(distances) == 2