class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()])
        s = s.lower()
        print(f"s: {s}")
        lp = 0
        rp = len(s) -1
        while rp-lp >= 1:
            if s[lp] != s[rp]:
                return False
            lp += 1
            rp -= 1
        return True