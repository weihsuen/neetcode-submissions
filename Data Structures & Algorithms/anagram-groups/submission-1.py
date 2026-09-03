class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #1. Sort all strings with that being the key. If same key, add the original string into the hashmap value and then print
        #Note: in python, strings = immutable, to sort, need to "".join
        myHash = {}
        for mystr in strs:
            i = "".join(sorted(mystr))
            myHash.setdefault(i, []).append(mystr)
        return list(myHash.values())




        #2. Have a hashmap storing string and hashmap of that string. Compare that hashmap and if same, put tgt
        