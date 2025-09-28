class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores character -> last seen index
        l = 0          # Left pointer of the sliding window
        longest = 0    # Maximum length found so far
        
        for r in range(len(s)):
            # If the current character s[r] is already in our map
            # AND its last seen index is >= l (meaning it's within the current window)
            if s[r] in char_map and char_map[s[r]] >= l:
                # Move the left pointer to the position after the last occurrence
                # This effectively removes the repeated character and everything before it
                l = char_map[s[r]] + 1
            
            # Update the last seen index of the current character
            char_map[s[r]] = r
            
            # Calculate the current window length and update the maximum
            longest = max(longest, r - l + 1)
            
        return longest