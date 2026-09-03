class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(l, path):
            if l == len(s):
                ans.append(path[:])
                return 

            for end in range(l,len(s)):
                substr = s[l:end+1]
                if substr == substr[::-1]:
                    path.append(substr)
                    backtrack(end+1, path)
                    path.pop()

            return 

        backtrack(0, [])
        return ans

            
        