class Solution(object):
    def totalFruit(self, fruits):
        count = {}
        left = 0
        ans = 0

        for right, fruit in enumerate(fruits):
            count[fruit] = count.get(fruit, 0) + 1

            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                left += 1

            ans = max(ans, right - left + 1)

        return ans