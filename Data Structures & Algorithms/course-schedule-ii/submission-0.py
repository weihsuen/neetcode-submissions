class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)] #store prereq for each node
        degree = [0] * numCourses

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            degree[course] +=1

        #count degree
        # for i in range(numCourses):
        #     degree[i] = len(adjList[i])

        q=deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)

        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            for i in adjList[cur]:
                degree[i] -=1
                if degree[i] == 0:
                    q.append(i)

        if len(ans) != numCourses:
            return []
        else:
            return ans


