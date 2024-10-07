class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) <= 2:
            return min(i for i in cost)
        one = cost[-1]
        two = cost[-2]
        # We already processed the first 2
        i = len(cost) - 3
        while i >= 0:
            temp = two
            two = min(temp, one)
            two += cost[i]
            one = temp
            i -= 1
        return min(two, one)
