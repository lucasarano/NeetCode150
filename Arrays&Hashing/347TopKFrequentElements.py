import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        myHeap = [] # Keep a heap to keep track of the k most frequent elements
        output = []

        # We count the numbers to get frequencies for each
        numbFreq = Counter(nums)

        # We order the numbers by putting them as negative in minheap making a maxheap
        for num, freq in numbFreq.items():
            newTup = (-freq, num)
            heapq.heappush(myHeap, newTup)

        
        # We loop until we find the k most frequent elements
        for a in range(k):
            newFreq, newNum = heapq.heappop(myHeap)
            output.append(newNum)
        return output