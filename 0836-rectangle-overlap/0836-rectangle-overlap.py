class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # rec1: [x1, y1, x2, y2]
        # rec2: [x3, y3, x4, y4]
        
        # Non-overlapping conditions check karna:
        is_left = rec1[2] <= rec2[0]   # rec1, rec2 ke poori tarah left mein hai
        is_right = rec1[0] >= rec2[2]  # rec1, rec2 ke poori tarah right mein hai
        is_below = rec1[3] <= rec2[1]  # rec1, rec2 ke poori tarah neeche hai
        is_above = rec1[1] >= rec2[3]  # rec1, rec2 ke poori tarah upar hai
        
        # Agar inmein se koi bhi true nahi hai, toh overlap ho raha hai
        return not (is_left or is_right or is_below or is_above)