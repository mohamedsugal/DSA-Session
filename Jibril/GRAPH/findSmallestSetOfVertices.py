class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        
        for src, dest in edges:
            indegree[dest] = indegree.get(dest, 0) + 1
        print(indegree)
        res = []
        
        for i in range(n):
            if i not in indegree:
                res.append(i)
        return res
        
        
        
        