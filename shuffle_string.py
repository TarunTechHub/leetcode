#1528. Shuffle String
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = list(s)
        l = len(s)
        for i in range(l):
            res[indices[i]] = s[i]
        return "".join(res)
