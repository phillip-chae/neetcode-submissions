class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            sor = ("").join(sorted(s))
            if not sor in d:
                d[sor] = [s]
            else:
                d[sor].append(s)
        return [
            v
            for v in d.values()
        ]