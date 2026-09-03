class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        #create AdjList
        adjList = [[] for i in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(cur, parent):
            if cur in visited:
                return False
            
            visited.add(cur)

            for i in adjList[cur]:
                if i != parent:
                    if not dfs(i, cur):
                        return False

            return True
        
        ans = dfs(0, None)

        if ans == False:
            return False

        if len(visited) != n:
            return False
        else:
            return True
        