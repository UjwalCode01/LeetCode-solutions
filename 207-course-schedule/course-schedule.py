from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Build adjacency list and compute in-degrees
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # Enqueue all courses with no prerequisites (in-degree == 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        processed_courses = 0
        
        while queue:
            curr = queue.popleft()
            processed_courses += 1
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If processed all courses, no cycle exists
        return processed_courses == numCourses