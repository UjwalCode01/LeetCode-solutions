class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        # Existing key ko override karega ya naya add karega
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        # Check karte hain ki konsi keys prefix se start ho rahi hain
        for k, v in self.map.items():
            if k.startswith(prefix):
                total += v
        return total
        