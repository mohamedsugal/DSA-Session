from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adjacency = {}
        for src,dest in edges:
            if src not in adjacency:
                adjacency[src] = []
            adjacency[dest] = src
            
        
        res = []   
        for k,v in adjacency.items():
            if v == []:
                res.append(k)
                
        return res
#Example 1
sol = Solution()

n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print("#Example 1")
print(sol.findSmallestSetOfVertices(n,edges))

#Example2
n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
print("#Example 2")
print(sol.findSmallestSetOfVertices(n,edges))