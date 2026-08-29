class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()

        i = 0
        min_radius = 0

        for house in houses:
            # Advance heater pointer if the next heater is closer to the house
            while i < len(heaters) - 1 and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
                i += 1
            
            # Distance from current house to its closest heater
            min_radius = max(min_radius, abs(heaters[i] - house))

        return min_radius