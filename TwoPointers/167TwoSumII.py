class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        result = []
        while i < j:
            current = numbers[i] + numbers[j]
            
            if current > target:
                j -= 1
            elif current < target:
                i += 1
            else:
                result.append(i + 1)
                result.append(j + 1)
                i += 1
                j -= 1
        return result