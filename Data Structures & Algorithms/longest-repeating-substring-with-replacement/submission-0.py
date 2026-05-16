class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]

            freq[char] = freq.get(char,0)+1

            max_freq = max(max_freq,freq[char])

            window_size = right - left + 1

            while window_size - max_freq > k:
                freq[s[left]]-=1
                left+=1
                window_size = right - left + 1
            
            longest = max(longest,window_size)
            
        return longest
