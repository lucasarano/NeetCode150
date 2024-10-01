class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        visited = set()
        for x in range(len(nums)):

            if x > 0 and nums[x] == nums[x - 1]:
                continue
            i = x + 1
            j = len(nums) - 1

            while i < j:
                if (nums[x] + nums[i] + nums[j]) > 0:
                    j -= 1
                elif (nums[x] + nums[i] + nums[j]) < 0:
                    i += 1
                else:
                    
                    result.append([nums[x], nums[i], nums[j]])
                    

                    # Skip duplicate 'i' values
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1

                    # Skip duplicate 'j' values
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                    
        return result