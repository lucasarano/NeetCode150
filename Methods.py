

# Heaps:
import heapq
myHeap = []
myList = [1,2,5,7,9]
element = 3

myHeap = heapq.heapify(myList) # Automatically a min heap (use - to make max heap)

heapq.heappush(myHeap, element) # Pushed element to heap
heapq.heappop(myHeap) # Pops prioritized element


# Characters

myStr = "Hello"
myStr.find("l") # This will return index for where l is in first occurance
myStr.isdigit()
myStr.isalnum()
myStr.isalpha()

char = "A"
myCharVal = ord(char)
myNewChar = chr(65) # From num to ascii

