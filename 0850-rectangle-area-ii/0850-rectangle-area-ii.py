class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))
            
        # Sort events by x-coordinate
        events.sort(key=lambda x: x[0])
        
        def get_active_height(intervals):
            if not intervals:
                return 0
            # Sort intervals by start y
            intervals.sort(key=lambda x: x[0])
            total_length = 0
            curr_y1, curr_y2 = intervals[0]
            
            for y1, y2 in intervals[1:]:
                if y1 < curr_y2:
                    curr_y2 = max(curr_y2, y2)
                else:
                    total_length += curr_y2 - curr_y1
                    curr_y1, curr_y2 = y1, y2
            total_length += curr_y2 - curr_y1
            return total_length

        active_intervals = []
        prev_x = events[0][0]
        total_area = 0
        MOD = 10**9 + 7
        
        i = 0
        while i < len(events):
            curr_x = events[i][0]
            width = curr_x - prev_x
            if width > 0:
                total_area += width * get_active_height(active_intervals)
                
            while i < len(events) and events[i][0] == curr_x:
                _, type_val, y1, y2 = events[i]
                if type_val == 1:
                    active_intervals.append((y1, y2))
                else:
                    active_intervals.remove((y1, y2))
                i += 1
                
            prev_x = curr_x
            
        return total_area % MOD