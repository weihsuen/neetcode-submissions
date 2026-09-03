class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapS = {}
        mapT = {}

        for n in s:
            mapS[n] = 1 + mapS.get(n,0)
        for n in t:
            mapT[n] = 1 + mapT.get(n,0)

        if mapS != mapT:
            return False
        else:
            return True