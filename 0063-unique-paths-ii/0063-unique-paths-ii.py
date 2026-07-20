class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # Grid ki dimensions nikalte hain
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # Agar start ya end position par hi obstacle hai, toh koi rasta nahi hai
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
            
        # Starting point par pahunchne ka 1 tarika hai
        obstacleGrid[0][0] = 1
        
        # Pehli row ke liye paths nikalte hain
        for c in range(1, n):
            # Agar obstacle nahi hai aur pichle cell se rasta aa raha hai
            if obstacleGrid[0][c] == 0:
                obstacleGrid[0][c] = obstacleGrid[0][c-1]
            else:
                obstacleGrid[0][c] = 0
                
        # Pehle column ke liye paths nikalte hain
        for r in range(1, m):
            if obstacleGrid[r][0] == 0:
                obstacleGrid[r][0] = obstacleGrid[r-1][0]
            else:
                obstacleGrid[r][0] = 0
                
        # Baaki bache hue poore grid ko fill karte hain
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 0:
                    # Current cell = Top cell + Left cell
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
                else:
                    # Agar obstacle hai toh yahan se aage koi rasta nahi jayega
                    obstacleGrid[r][c] = 0
                    
        # Bottom-right corner mein humara final answer hoga
        return obstacleGrid[m-1][n-1]
        