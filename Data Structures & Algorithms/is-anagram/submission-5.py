class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. sort both strings and check is same... --> O(nlogn)
        if sorted(s) == sorted(t):
            return True
        return False

        #2. hashmap aka dict
        # hashS, hashT = {},{}

        # for c in s: #O(n)
        #     hashS[c] = hashS.get(c,0) + 1

        # for c in t: #O(n)
        #     hashT[c] = hashT.get(c,0) + 1
        
        # return hashT == hashS



        