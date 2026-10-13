class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        char_s, char_t = dict(), dict()
        for i in range(len(s)):
            if s[i] in char_s:
                char_s[s[i]] += 1
            else:
                char_s[s[i]] = 1
            if t[i] in char_t:
                char_t[t[i]] += 1
            else:
                char_t[t[i]] = 1
        return char_s == char_t