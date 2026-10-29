class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        swaps = 0
        # Create a hash map to quickly find the current index of any person's ID
        pos = {val: i for i, val in enumerate(row)}
        
        for i in range(0, len(row), 2):
            first_person = row[i]
            # Partner of 2k is 2k+1, and partner of 2k+1 is 2k. 
            # Bitwise XOR with 1 achieves this for any integer.
            partner = first_person ^ 1
            
            # Check if the person sitting next to first_person is NOT their partner
            if row[i + 1] != partner:
                swaps += 1
                
                # Find where the actual partner is currently sitting
                partner_pos = pos[partner]
                
                # Swap the person currently sitting at i + 1 with the actual partner
                row[i + 1], row[partner_pos] = row[partner_pos], row[i + 1]
                
                # Update the position hash map for the person who got moved
                pos[row[partner_pos]] = partner_pos
                
        return swaps