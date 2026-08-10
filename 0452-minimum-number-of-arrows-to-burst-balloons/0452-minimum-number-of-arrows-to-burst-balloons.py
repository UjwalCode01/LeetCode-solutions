class Solution(object):

    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Step 1: Sort balloons by their ending coordinates
        points.sort(key=lambda x: x[1])

        arrows = 1
        # Position of the arrow shot
        prev_end = points[0][1]

        # Step 2: Iterate through balloons and check for overlap
        for start, end in points[1:]:
            # If the current balloon starts after the last arrow shot position,
            # shoot a new arrow at the end of the current balloon
            if start > prev_end:
                arrows += 1
                prev_end = end

        return arrows