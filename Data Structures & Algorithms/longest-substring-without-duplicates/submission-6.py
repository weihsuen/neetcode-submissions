class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        left = 0 
        right =1
        mymax = 0
        myset = set()
        myset.add(s[left])

        while right < len(s):
            if s[right] in myset:
                while s[right] in myset:
                    myset.remove(s[left])
                    left +=1
            myset.add(s[right])
            mymax = max(mymax, right-left+1)
            right+=1

        return mymax