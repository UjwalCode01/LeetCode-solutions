class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(st: str) -> str:
            res = []
            for char in st:
                if char != '#':
                    res.append(char)
                elif res:
                    res.pop()
            return "".join(res)
            
        return build(s) == build(t)