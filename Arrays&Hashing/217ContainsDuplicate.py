class Solution:

    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False


# Testing
solution = Solution()
print(solution.containsDuplicate([1, 2, 2, 3, 5, 8]))