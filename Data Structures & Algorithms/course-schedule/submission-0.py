class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for i, prereq in prerequisites:
            adjList[i].append(prereq)

        visited = set()


        def dfs(cur):
            if cur in visited:
                return False
            if adjList[cur] == []:
                return True

            visited.add(cur)

            for prereq in adjList[cur]:
                if not dfs(prereq):
                    return False

            visited.remove(cur)
            adjList[cur] = []
            return  True

        for courses in range(numCourses):
            if not dfs(courses):
                return False

        return True



                