from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # First we count the number of chars we need to find
        result = ""  # Empty result to store the min window
        chars = Counter(t)  # Count of characters in t
        found = Counter()  # To keep track of characters found in s
        i = 0
        j = 0
        min_len = float('inf')  # Start with an infinitely large window size

        while i < len(s):
            print(f"Running with i = {i} and j = {j} and found = {found}")
            found[s[i]] += 1

            # Check if the current window contains all characters in t
            while all(found[char] >= chars[char] for char in chars):
                # We found a valid window
                print(f"Found valid window: {found} contains {chars}")

                if i - j + 1 < min_len:  # Update result if current window is smaller
                    min_len = i - j + 1
                    result = s[j:i+1]  # Fix the substring to include s[i]
                    print(f"Updated result to {result}")
                
                # Move the left pointer to try and shrink the window
                if s[j] in found:
                    found[s[j]] -= 1
                j += 1

            i += 1

        return result
