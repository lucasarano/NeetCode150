class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 3:
            return max(profit for profit in nums)
        
        one = nums[0]
        two = max(nums[0], nums[1])
        i = 2
        while i < len(nums) - 1:
            
            maximum = max(one + nums[i], two)
            one = two
            two = maximum
            i += 1
        minFirst = two
        one = nums[1]
        two = max(nums[1], nums[2])
        i = 3
        while i < len(nums):
            
            maximum = max(one + nums[i], two)
            one = two
            two = maximum
            i += 1
        return max(two, minFirst)

            
