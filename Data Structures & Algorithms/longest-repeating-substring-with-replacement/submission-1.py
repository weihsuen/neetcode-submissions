class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myhash = defaultdict(int)
        max_count = window = 0
        l = r = 0

        while r < len(s):
            myhash[s[r]] +=1
            max_count = max(max_count, myhash[s[r]])
            #if (r-l+1) - max_count > k:
            while (r-l+1) - max_count >k:
                myhash[s[l]] -=1
                max_count = max(max_count, myhash[s[l]])
                l+=1
            window = max(window, r-l+1)
            r+=1

        return window
        