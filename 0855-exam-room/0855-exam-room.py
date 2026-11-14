class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            self.students.append(0)
            return 0
        
        max_dist = self.students[0]
        best_seat = 0
        
        for i in range(len(self.students) - 1):
            prev = self.students[i]
            curr = self.students[i + 1]
            dist = (curr - prev) // 2
            
            if dist > max_dist:
                max_dist = dist
                best_seat = prev + dist
                
        if self.n - 1 - self.students[-1] > max_dist:
            best_seat = self.n - 1
            
        self.students.append(best_seat)
        self.students.sort()
        return best_seat

    def leave(self, p: int) -> None:
        self.students.remove(p)