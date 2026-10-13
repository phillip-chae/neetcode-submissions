class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        for c in t:
            if c in d and d[c] > 0:
                d[c] -= 1
            else:
                return False
        
        if any(d[c] != 0 for c in d): return False
        return True