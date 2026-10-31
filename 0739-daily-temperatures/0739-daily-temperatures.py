class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # indices store karega
        
        for i, temp in enumerate(temperatures):
            # Jab tak current temp stack ke top index ke temp se bada hai
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            
            stack.append(i)
            
        return answer