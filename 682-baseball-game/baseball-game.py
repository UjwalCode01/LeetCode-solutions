class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        
        for op in operations:
            if op == '+':
                # Last 2 scores ka sum
                record.append(record[-1] + record[-2])
            elif op == 'D':
                # Last score ka double
                record.append(2 * record[-1])
            elif op == 'C':
                # Last score ko invalidate/remove karna
                record.pop()
            else:
                # Agar koi number (integer) string ke roop me aaye
                record.append(int(op))
                
        # Total scores ka sum return karenge
        return sum(record)
        