class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            
            if tx > ty:
                # If sy can be reached and remaining difference is a multiple of ty
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                # If sx can be reached and remaining difference is a multiple of tx
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
                    
        return False