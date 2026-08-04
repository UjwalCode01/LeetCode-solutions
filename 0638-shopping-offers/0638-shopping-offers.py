class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        memo = {}

        def dfs(cur_needs):
            # Tuple bana ke memoize karne ke liye key use karenge
            needs_tuple = tuple(cur_needs)
            if needs_tuple in memo:
                return memo[needs_tuple]

            # Direct purchase cost (bina kisi offer ke)
            min_cost = sum(cur_needs[i] * price[i] for i in range(len(price)))

            # Special offers try karo
            for offer in special:
                clone_needs = list(cur_needs)
                is_valid = True

                for i in range(len(price)):
                    # Agar offer mein item count need se zyaada hai, to skip
                    if offer[i] > clone_needs[i]:
                        is_valid = False
                        break
                    clone_needs[i] -= offer[i]

                # Agar offer apply kar sakte hain
                if is_valid:
                    offer_cost = offer[-1]
                    min_cost = min(min_cost, offer_cost + dfs(clone_needs))

            memo[needs_tuple] = min_cost
            return min_cost

        return dfs(needs)