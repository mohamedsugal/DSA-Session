from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = {}
        
        for src,dest in edges:
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []
                
            graph[src].append(dest)
            graph[dest].append(src)
            
        
        for k,v in graph.items():
            if len(v) > 1:
                return k

sol = Solution()
# Example 1
edges = [[1,2],[2,3],[4,2]]
print(sol.findCenter(edges))

#example 2
edges = [[1,2],[5,1],[1,3],[1,4]]
print(sol.findCenter(edges))