class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) <= 2:
            return max(nums[0], nums[1])
        one = nums[0]
        two = max(one, nums[1])
        i = 2
        money = 0
        while i < len(nums):
            money = max(nums[i] + one, two)
            one = two
            two = money
            i += 1
        return two