class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26

        for letter in s:
            idx = ord(letter)-ord('a')
            freq[idx]+=1

        for letter in t:
            idx = ord(letter)-ord('a')
            freq[idx]-=1

        for value in freq:
            if value != 0:
                return False
        
        return True
