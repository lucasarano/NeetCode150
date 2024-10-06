import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        myHeap = []
        output = []

        numbFreq = Counter(nums)

        for num, freq in numbFreq.items():
            newTup = (-freq, num)
            heapq.heappush(myHeap, newTup)

        
        for a in range(k):
            newFreq, newNum = heapq.heappop(myHeap)
            output.append(newNum)
        return output