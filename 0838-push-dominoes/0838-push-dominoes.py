class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = ['L'] + [c for c, ch in enumerate(dominoes) if ch != '.'] + ['R']
        # Wait, let's keep track of characters and their indices properly:
        # A cleaner two-pointer / force-propagation approach:
        
        n = len(dominoes)
        forces = [0] * n
        
        # Scan from left to right to calculate rightward forces from 'R'
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
            
        # Scan from right to left to calculate leftward forces from 'L'
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
            
        # Construct result based on net forces
        res = []
        for f in forces:
            if f > 0:
                res.append('R')
            elif f < 0:
                res.append('L')
            else:
                res.append('.')
                
        return "".join(res)