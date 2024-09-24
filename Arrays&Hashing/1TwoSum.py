class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = {}
        result = []
        # Create a dictionary with indexes as values and then key is number
        for i in range(len(nums)):
            if target - nums[i] in index:
                print("found in index")
                for n in index[target - nums[i]]:
                    result.append(n)
                result.append(i)
            if nums[i] not in index:
                index[nums[i]] = [i]
                # We are assigning each number to a list of places where its found
            else:
                index[nums[i]].append(i)
            # Appending the new index found with repeat
        
        
        return result