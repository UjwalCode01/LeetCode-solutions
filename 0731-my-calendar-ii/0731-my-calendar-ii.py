class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Check if the new event conflicts with any existing double bookings (triple booking check)
        for start, end in self.overlaps:
            if max(start, startTime) < min(end, endTime):
                return False
        
        # Check against existing bookings to find new overlapping intervals
        for start, end in self.bookings:
            if max(start, startTime) < min(end, endTime):
                # Add the overlapping intersection to our double-booking list
                self.overlaps.append((max(start, startTime), min(end, endTime)))
        
        # If no triple booking occurs, add the event to bookings and return True
        self.bookings.append((startTime, endTime))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime, endTime)