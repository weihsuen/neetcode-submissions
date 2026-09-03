class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #Form Adj List
        adjList = [[] for _ in range(n)]
        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        

        #def dfs
        visited = set()
        def dfs(cur, parent):
            visited.add(cur)

            for neighbours in adjList[cur]:
                if neighbours not in visited and neighbours != parent:
                    dfs(neighbours, cur)

        #Iterate through all nodes
        count = 0
        for node in range(n):
            if node not in visited:
                count +=1
                dfs(node, node)

        return count



