class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) #key is sorted, value is the actual string

        for s in strs:
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)

        return res.values()
        
        