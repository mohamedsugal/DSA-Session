class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        q = deque([[0]])
        res = []
        
        destNode = len(graph) - 1
        while q:
            path = q.popleft()
            if path[-1] == destNode:
                res.append(path)
            else:
                for neighbor in graph[path[-1]]:
                    q.append(path + [neighbor])
        return res