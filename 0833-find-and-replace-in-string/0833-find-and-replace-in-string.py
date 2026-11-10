class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Indices, sources, aur targets ko zip karke reverse order mein sort kar rahe hain (index ke basis par)
        ops = sorted(zip(indices, sources, targets), reverse=True)
        
        # String ko list mein convert kar rahe hain taaki slice replacement aasan ho
        res = list(s)
        
        for idx, src, tgt in ops:
            # Check kar rahe hain ki kya string ke us index par source match kar raha hai
            if s[idx:idx + len(src)] == src:
                # Agar match ho raha hai, toh portion ko target se replace kar do
                res[idx : idx + len(src)] = list(tgt)
                
        return "".join(res)