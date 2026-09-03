"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        created = {}
        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node == None:
                return None

            mynewnode = Node(node.val, [])
            created[node] = mynewnode
            for neighbours in node.neighbors:
                if neighbours not in created:
                    newnode = dfs(neighbours)
                    created[neighbours] = newnode

                mynewnode.neighbors.append(created[neighbours])

            return mynewnode

        
        return dfs(node)
                

