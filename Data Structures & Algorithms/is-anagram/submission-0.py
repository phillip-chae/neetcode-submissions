class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_1 = sorted([c for c in s])
        t_1 = sorted([c for c in t])
        return s_1 == t_1
