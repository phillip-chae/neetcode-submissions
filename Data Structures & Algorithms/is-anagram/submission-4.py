class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars= dict()
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        
        for c in t:
            if c in chars and chars[c] > 0:
                chars[c] -= 1
            else:
                return False
            if chars[c] == 0:
                del chars[c]
        
        return not bool(chars)