class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Check for any overlap with existing bookings
        for start, end in self.calendar:
            # Two half-open intervals [start, end) and [startTime, endTime) overlap 
            # if max(start, startTime) < min(end, endTime)
            if max(start, startTime) < min(end, endTime):
                return False
        
        # If no overlap, add the event and return True
        self.calendar.append((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime, endTime)