from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        stack = [(0,[0])]
        paths = []
        target = len(graph) - 1
        
        while stack:
            src,path = stack.pop()
            if src == target:
                paths.append(path)
            for n in graph[src]:
                stack.append((n,path+[n]))
                
        return paths

sol = Solution()
# Example 1
graph = [[1,2],[3],[3],[]]
print("#Example 1")
print(sol.allPathsSourceTarget(graph))

print("#Example 2")
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(sol.allPathsSourceTarget(graph))
