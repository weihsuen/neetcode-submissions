class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def union(x,y):
            parX = find(x)
            parY = find(y)
            parent[parX] = parY

        def find(x):
            while parent[x] != x:
                x = parent[parent[x]]
            return x
        
        n = max(max(x,y) for x,y in edges)

        parent = [x for x in range(n+1)]
        for x,y in edges:
            if find(x) == find(y):
                return [x,y]
            union(x,y)

        
            